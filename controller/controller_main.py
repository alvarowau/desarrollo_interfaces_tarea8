from datetime import datetime

from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import (
    QHeaderView,
    QWidget,
)

from controller.controller_datos import ControladorDatos
from repository.conection_mysql import AlumnoDAO, ConexionMySQL
from ui.ui_main import Ui_ui_main
from util.leer_archivo import CargadorCSV
from util.tratar_fecha import (
    calcular_diferencia_tiempo,
    transformar_a_segundos,
    transformar_a_segundos_desde_csv,
    transformar_segundos_a_fecha,
)


class ControladorMain(QWidget):
    """Controlador principal de la aplicación que gestiona la interfaz de alumnos.

    Esta clase maneja:
    - La visualización de la lista de alumnos en una tabla
    - La carga de datos desde archivos CSV
    - La navegación a detalles de alumnos
    - La gestión de la conexión a base de datos

    Attributes:
        fecha_actual (datetime): Fecha actual al inicializar el controlador.
        data_base (ConexionMySQL): Objeto para manejar la conexión a la base de datos.
        conexion: Conexión activa a la base de datos.
        alumno_dao (AlumnoDAO): Data Access Object para operaciones con alumnos.
        ui (Ui_ui_main): Interfaz de usuario generada por Qt.
        modelo (QStandardItemModel): Modelo de datos para la tabla de alumnos.
    """

    def __init__(self, data_base: ConexionMySQL):
        """Inicializa el controlador principal.

        Args:
            data_base (ConexionMySQL): Objeto de conexión a la base de datos.
        """
        super().__init__()
        self.fecha_actual = datetime.now()
        self.data_base = data_base
        self.conexion = self.data_base.conectar()
        self.alumno_dao = AlumnoDAO(self.conexion)
        self.ui = Ui_ui_main()
        self.ui.setupUi(self)
        self._conectar_senales()
        self._configurar_tabla()
        self.actualizar_tabla()

    def _configurar_tabla(self):
        """Configura la tabla de alumnos con sus columnas y propiedades."""
        self.modelo = QStandardItemModel()
        self.modelo.setColumnCount(4)
        self.modelo.setHorizontalHeaderLabels(
            ["ID", "Nombre", "Correo", "Última conexión"]
        )

        self.ui.tabla_Alumno.setModel(self.modelo)
        self.ui.tabla_Alumno.setColumnHidden(0, True)
        self.ui.tabla_Alumno.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch  # type: ignore
        )

    def _conectar_senales(self):
        """Conecta las señales de los botones a sus métodos correspondientes."""
        self.ui.button_salir.clicked.connect(self.cerrar)
        self.ui.butto_mostrar.clicked.connect(self.solicitar_alumno)
        self.ui.button_cargar.clicked.connect(self.cargar_archivos)
        self.ui.button_eliminar.clicked.connect(self.eliminar_tabla)

    def cerrar(self):
        """Cierra la conexión a la base de datos y la ventana actual."""
        if self.data_base:
            self.data_base.cerrar()
        self.close()

    def eliminar_tabla(self):
        """Elimina todos los registros de alumnos de la base de datos y limpia la tabla."""
        self.alumno_dao.eliminar_todos()
        self.limpiar_tabla()

    def solicitar_alumno(self):
        """Muestra los detalles del alumno seleccionado en la tabla.

        Abre una nueva ventana con la información detallada del alumno seleccionado.
        """
        indices = self.ui.tabla_Alumno.selectionModel().selectedIndexes()

        if not indices:
            return  # No hay selección

        fila = indices[0].row()
        id_alumno = self.modelo.item(fila, 0).text()
        alumno = self.alumno_dao.buscar_alumno_id(id_alumno)

        self.mostrar = ControladorDatos(alumno)
        self.mostrar.show()

    def actualizar_tabla(self):
        """Actualiza el contenido de la tabla con los datos actuales de la base de datos.

        Maneja posibles errores durante la actualización mostrando un mensaje al usuario.
        """
        try:
            alumnos = self.alumno_dao.listar_alumnos()
            self.limpiar_tabla()
            for a in alumnos:
                self.preparar_fila(a)
        except Exception as e:
            from PySide6.QtWidgets import QMessageBox

            QMessageBox.critical(self, "Error al actualizar la tabla", str(e))

    def limpiar_tabla(self):
        """Limpia completamente el modelo de la tabla y restablece los encabezados."""
        self.modelo.clear()
        self.modelo.setColumnCount(4)
        self.modelo.setHorizontalHeaderLabels(
            ["ID", "Nombre", "Correo", "Última conexión"]
        )

    def cargar_archivos(self):
        """Carga datos de alumnos desde un archivo CSV a la base de datos.

        Utiliza la clase CargadorCSV para seleccionar y leer el archivo,
        luego inserta los datos en la base de datos y actualiza la tabla.
        """
        cargador = CargadorCSV(self)
        datos = cargador.datos
        if not datos:
            return
        for dato in datos:
            self.alumno_dao.insertar_alumno(dato)
        self.actualizar_tabla()

    def preparar_fila(self, alumno: dict):
        """Prepara los datos de un alumno para ser mostrados en la tabla.

        Args:
            alumno (dict): Diccionario con los datos del alumno.
        """
        id_alumno = int(alumno["ID"])
        nombre = alumno["Alumno"]
        correo = alumno["Correo"]
        ultimo_acceso = transformar_a_segundos_desde_csv(
            alumno["UltimoAcceso"], self.fecha_actual
        )
        ultimo_acceso = transformar_segundos_a_fecha(ultimo_acceso)
        segundos = transformar_a_segundos(self.fecha_actual)
        actual = transformar_segundos_a_fecha(segundos)
        diferencia = calcular_diferencia_tiempo(actual, ultimo_acceso)
        self.agregar_fila_tabla(id_alumno, nombre, correo, diferencia)

    def agregar_fila_tabla(
        self, id_alumno: int, nombre: str, correo: str, ultima_conexion: str
    ):
        """Añade una fila con los datos de un alumno a la tabla.

        Args:
            id_alumno (int): Identificador único del alumno.
            nombre (str): Nombre completo del alumno.
            correo (str): Correo electrónico del alumno.
            ultima_conexion (str): Tiempo desde la última conexión del alumno.
        """
        fila = [
            QStandardItem(str(id_alumno)),
            QStandardItem(nombre),
            QStandardItem(correo),
            QStandardItem(ultima_conexion),
        ]
        self.modelo.appendRow(fila)
