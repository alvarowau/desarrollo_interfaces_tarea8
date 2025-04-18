import mysql.connector
from mysql.connector import Error


class ConexionMySQL:
    """
    Clase para gestionar la conexión con una base de datos MySQL.

    Esta clase proporciona métodos para conectar y cerrar una conexión a una base de datos MySQL.

    Atributos:
        config (dict): Configuración de la conexión con la base de datos.
        conexion (mysql.connector.connection.MySQLConnection | None): Objeto de conexión MySQL.

    Métodos:
        conectar(): Establece la conexión con la base de datos MySQL y la devuelve.
        cerrar(): Cierra la conexión con la base de datos si está abierta.
    """

    def __init__(
        self,
        host="localhost",
        user="alvaro",
        password="alvaro",
        database="acceso",
        port=3306,
    ):
        """
        Inicializa la configuración de la conexión.

        Args:
            host (str): Dirección del host del servidor de base de datos. Por defecto "localhost".
            user (str): Usuario para la conexión. Por defecto "alvaro".
            password (str): Contraseña para la conexión. Por defecto "alvaro".
            database (str): Nombre de la base de datos. Por defecto "acceso".
            port (int): Puerto para la conexión. Por defecto 3306.
        """
        self.config = {
            "host": host,
            "user": user,
            "password": password,
            "database": database,
            "port": port,
        }
        self.conexion = None

    def conectar(self):
        """
        Establece la conexión con la base de datos MySQL.

        Returns:
            mysql.connector.connection.MySQLConnection | None:
                La conexión a la base de datos MySQL si es exitosa,
                de lo contrario None en caso de error.
        """
        try:
            self.conexion = mysql.connector.connect(**self.config)
            return self.conexion
        except Error:
            return None

    def cerrar(self):
        """
        Cierra la conexión a la base de datos MySQL si está abierta.

        Este método no devuelve ningún valor.
        """
        if self.conexion:
            self.conexion.close()


class AlumnoDAO:
    """
    Data Access Object para gestionar operaciones sobre la tabla 'alumnos' en la base de datos.

    Esta clase proporciona métodos para insertar, eliminar, buscar y listar alumnos de la base de datos.

    Atributos:
        conexion (mysql.connector.connection.MySQLConnection): Conexión activa con la base de datos.
        cursor (mysql.connector.cursor.MySQLCursor): Cursor para ejecutar las consultas SQL.

    Métodos:
        insertar_alumno(alumno): Inserta un nuevo alumno en la base de datos.
        eliminar_todos(): Elimina todos los registros de la tabla 'alumnos'.
        buscar_alumno_id(id_): Busca un alumno por su ID.
        listar_alumnos(): Retorna una lista de todos los alumnos registrados.
        buscar_por_nombre(nombre): Busca un alumno por su nombre.
        cerrar(): Cierra el cursor utilizado para ejecutar las consultas.
    """

    def __init__(self, conexion):
        """
        Inicializa el objeto DAO con una conexión activa a la base de datos.

        Args:
            conexion (mysql.connector.connection.MySQLConnection): Conexión activa a la base de datos.
        """
        self.conexion = conexion
        self.cursor = self.conexion.cursor()

    def insertar_alumno(self, alumno: dict):
        """
        Inserta un nuevo alumno en la tabla 'alumnos'.

        Args:
            alumno (dict): Diccionario con los datos del alumno. Debe contener las claves "ID", "Alumno", "Correo", y "UltimoAcceso".
        """
        is_id_disponible = self.__id_disponible(alumno["ID"])
        if is_id_disponible:
            query = """
                INSERT INTO alumnos (ID, Alumno, Correo, UltimoAcceso)
                VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(
                query,
                (
                    alumno["ID"],
                    alumno["Alumno"],
                    alumno["Correo"],
                    alumno["UltimoAcceso"],
                ),
            )
            self.conexion.commit()

    def eliminar_todos(self):
        """
        Elimina todos los registros de la tabla 'alumnos'.

        Este método no recibe parámetros ni devuelve valor.
        """
        self.cursor.execute("DELETE FROM alumnos")
        self.conexion.commit()

    def buscar_alumno_id(self, id_) -> dict:
        """
        Busca un alumno por su ID.

        Args:
            id_ (int): El ID del alumno a buscar.

        Returns:
            dict | None: Un diccionario con los datos del alumno si se encuentra, de lo contrario None.
        """
        cursor_dict = self.conexion.cursor(dictionary=True)
        cursor_dict.execute("SELECT * FROM alumnos WHERE ID = %s", (id_,))
        resultado = cursor_dict.fetchone()
        return resultado

    def listar_alumnos(self):
        """
        Retorna una lista de diccionarios con los datos de todos los alumnos.

        Returns:
            list: Lista de diccionarios, donde cada diccionario contiene los datos de un alumno.
        """
        cursor_dict = self.conexion.cursor(dictionary=True)
        cursor_dict.execute("SELECT * FROM alumnos")
        resultado = cursor_dict.fetchall()
        cursor_dict.close()
        return resultado

    def __id_disponible(self, id_alumno):
        """
        Verifica si un ID de alumno está disponible en la base de datos.

        Args:
            id_alumno (int): El ID del alumno a verificar.

        Returns:
            bool: True si el ID está disponible, False si ya existe en la base de datos.
        """
        query = "SELECT EXISTS(SELECT 1 FROM alumnos WHERE ID = %s) AS existe"
        cursor = self.conexion.cursor()
        cursor.execute(query, (id_alumno,))
        resultado = cursor.fetchone()
        if resultado and resultado[0] == 1:
            return False
        else:
            return True

    def buscar_por_nombre(self, nombre):
        """
        Busca un alumno por nombre.

        Args:
            nombre (str): El nombre del alumno a buscar.

        Returns:
            dict | None: Un diccionario con los datos del alumno si se encuentra, de lo contrario None.
        """
        query = "SELECT * FROM alumnos WHERE Alumno = %s"
        self.cursor.execute(query, (nombre,))
        return self.cursor.fetchone()

    def cerrar(self):
        """
        Cierra el cursor utilizado para ejecutar las consultas.

        Este método no devuelve ningún valor.
        """
        self.cursor.close()
