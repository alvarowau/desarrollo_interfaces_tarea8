from PySide6.QtWidgets import QMessageBox, QWidget

from controller.controller_main import ControladorMain
from repository.conection_mysql import ConexionMySQL
from ui.ui_conection import Ui_ui_conection


class ControladorConexion(QWidget):
    """Controlador para la interfaz de conexión a base de datos MySQL.

    Esta clase maneja:
    - La interfaz de usuario para ingresar credenciales de conexión
    - La validación de los datos ingresados
    - El establecimiento de la conexión con la base de datos
    - La gestión de reintentos fallidos

    Attributes:
        conexion (object): Objeto de conexión a la base de datos.
        intentos_conexion (int): Contador de intentos de conexión fallidos.
        max_intentos (int): Límite máximo de intentos permitidos.
        ui (Ui_ui_conection): Instancia de la interfaz de usuario generada por Qt.
    """

    def __init__(self):
        """Inicializa el controlador de conexión.

        Configura la interfaz de usuario y establece los valores iniciales.
        """
        super().__init__()
        self.ui = Ui_ui_conection()
        self.ui.setupUi(self)
        self.conexion = None  # Inicializar la conexión
        self.ui.button_conectar.clicked.connect(self.intento_conexion)
        self.intentos_conexion = 0
        self.max_intentos = 3
        self.cargar_datos()

    def cargar_datos(self):
        """Carga datos predeterminados en los campos del formulario."""
        self.ui.line_host.setText("localhost")
        self.ui.line_user.setText("alvaro")
        self.ui.line_password.setText("alvaro")
        self.ui.line_database.setText("acceso")
        self.ui.line_port.setText("3306")

    def intento_conexion(self):
        """Intenta establecer conexión con la base de datos.

        Maneja:
        - Límite de intentos fallidos
        - Conversión de tipos de datos
        - Apertura de la ventana principal si la conexión es exitosa
        """
        if self.intentos_conexion >= self.max_intentos:
            self.mostrar_error(
                f"No se pudo conectar después de {self.max_intentos} intentos."
            )
            self.close()
            return

        datos = self.obtener_datos_formulario()
        if datos:
            try:
                port = int(datos["port"])
                base_datos = ConexionMySQL(
                    host=datos["host"],
                    user=datos["user"],
                    password=datos["password"],
                    database=datos["database"],
                    port=port,
                )
                self.conexion = base_datos.conectar()
                if self.conexion:
                    self.mostrar_mensaje("Conexión exitosa")
                    self.main = ControladorMain(data_base=base_datos)
                    self.main.show()
                    self.close()
                else:
                    self.intentos_conexion += 1
                    self.mostrar_error(
                        f"Intento {self.intentos_conexion}/{self.max_intentos}: No se pudo conectar a la base de datos. Verifica los datos."
                    )
            except ValueError:
                self.mostrar_error("El puerto debe ser un número entero.")
                return
        else:
            return

    def obtener_datos_formulario(self):
        """Recoge y valida los datos ingresados en el formulario.

        Returns:
            dict or None: Diccionario con los datos validados o None si hay campos vacíos.

            El diccionario contiene:
                - host (str)
                - user (str)
                - password (str)
                - database (str)
                - port (str)
        """
        datos = {
            "host": self.ui.line_host.text(),
            "user": self.ui.line_user.text(),
            "password": self.ui.line_password.text(),
            "database": self.ui.line_database.text(),
            "port": self.ui.line_port.text(),
        }

        campos_vacios = [clave for clave, valor in datos.items() if not valor]

        if campos_vacios:
            self.mostrar_error(
                f"Los siguientes campos están vacíos: {', '.join(campos_vacios)}"
            )
            return None

        return datos

    def mostrar_mensaje(self, texto):
        """Muestra un mensaje de información al usuario.

        Args:
            texto (str): Mensaje a mostrar.
        """
        QMessageBox.information(self, "Información", texto)

    def mostrar_error(self, texto):
        """Muestra un mensaje de error al usuario.

        Args:
            texto (str): Mensaje de error a mostrar.
        """
        QMessageBox.critical(self, "Error", texto)

    def closeEvent(self, event):
        """Maneja el evento de cierre de la ventana.

        Args:
            event (QCloseEvent): Evento de cierre.
        """
        if self.conexion:
            self.conexion.close()
        event.accept()
