from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
import csv


class CargadorCSV(QWidget):
    """
    Clase para cargar y leer archivos CSV en una interfaz gráfica utilizando PySide6.

    Esta clase permite seleccionar un archivo CSV y cargar sus datos. Los datos se almacenan
    en un atributo `datos` como una lista de diccionarios, donde cada diccionario representa
    una fila del archivo CSV con las cabeceras como claves.

    Atributos:
        datos (list | None): Lista de diccionarios con los datos del archivo CSV. Inicialmente es None.

    Métodos:
        leer_archivo(): Permite al usuario seleccionar un archivo CSV y cargar su contenido.
    """

    def __init__(self, parent=None):
        """
        Inicializa la clase y ejecuta el proceso de lectura del archivo CSV.

        Args:
            parent (QWidget, optional): El widget padre para la clase. El valor por defecto es None.
        """
        super().__init__(parent)
        self.datos = None
        self.leer_archivo()

    def leer_archivo(self):
        """
        Muestra un diálogo para seleccionar un archivo CSV y carga sus datos.

        Si el archivo se selecciona correctamente y contiene datos, se almacenan en el
        atributo `datos` y se muestra un mensaje de éxito. Si el archivo está vacío,
        se muestra una advertencia. Si ocurre un error al intentar leer el archivo,
        se muestra un mensaje de error.

        Este método no recibe ningún parámetro ni devuelve valores.

        Excepciones:
            Si ocurre un error al abrir o leer el archivo CSV, se captura la excepción
            y se muestra un mensaje de error en la interfaz gráfica.
        """
        archivo, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar archivo", "", "CSV (*.csv)"
        )
        if not archivo:
            QMessageBox.warning(
                self, "Archivo no seleccionado", "No se seleccionó ningún archivo."
            )
            return

        try:
            with open(archivo, newline="", encoding="utf-8") as f:
                lector = csv.DictReader(f)
                datos = [fila for fila in lector]

            if datos:
                self.datos = datos
                QMessageBox.information(self, "Éxito", "Archivo leído correctamente.")
            else:
                QMessageBox.warning(
                    self, "Archivo vacío", "El archivo CSV no contiene datos."
                )

        except Exception as e:
            QMessageBox.critical(
                self, "Error", f"No se pudo leer el archivo:\n{str(e)}"
            )
