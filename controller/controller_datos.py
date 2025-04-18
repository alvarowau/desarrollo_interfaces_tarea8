from datetime import datetime, timedelta

from PySide6.QtWidgets import QWidget

from ui.ui_datos import Ui_w_datos


class ControladorDatos(QWidget, Ui_w_datos):
    """Controlador para la ventana de visualización de datos detallados de un alumno.

    Muestra información detallada de un alumno incluyendo:
    - Nombre completo
    - Correo electrónico
    - Fecha y hora actual
    - Fecha y hora del último acceso calculada

    Attributes:
        alumno (dict): Diccionario con los datos del alumno.
    """
    def __init__(self, alumno: dict):
        """Inicializa el controlador con los datos del alumno.

        Args:
            alumno (dict): Diccionario con los datos del alumno que debe contener:
                - "Alumno": Nombre completo del alumno
                - "Correo": Correo electrónico
                - "UltimoAcceso": Cadena de tiempo del último acceso
        """
        super().__init__()
        self.setupUi(self)
        self.alumno = alumno
        nombre = alumno["Alumno"]
        email = alumno["Correo"]
        fecha_hora_actual = datetime.now()
        fecha_hora_formateada = fecha_hora_actual.strftime("%d-%m-%Y %H:%M:%S")
        fecha_hora_ultimo_acceso_formateada = self.calculo_ultima_conexion(
            fecha_hora_actual
        )

        self.label_fecha_actual.setText(fecha_hora_formateada)
        self.label_nombre.setText(nombre)
        self.label_correo.setText(email)
        self.label_ultima.setText(fecha_hora_ultimo_acceso_formateada)
        self.pushButton.clicked.connect(self.salir)

    def salir(self):
        """Cierra la ventana actual de la aplicación.

        Este método es invocado al hacer clic en el botón 'Salir'.
        """
        self.close()

    def calculo_ultima_conexion(self, fecha_hora_actual):
        """Calcula la fecha/hora del último acceso basado en el tiempo transcurrido.

        Procesa la cadena de tiempo del último acceso (ej: "2 días 3 horas 10 minutos")
        y calcula la fecha/hora exacta restando ese tiempo a la fecha actual.

        Args:
            fecha_hora_actual (datetime): Fecha y hora de referencia para el cálculo.

        Returns:
            str: Fecha formateada del último acceso o mensaje de error si no se puede calcular.

        Examples:
        >>> alumno = {"ID": 1, "Alumno": "Philip J. Fry", "Correo": "fry@planetexpress.com", "UltimoAcceso": ""}
        >>> controlador = ControladorDatos(alumno)
        >>> controlador.calculo_ultima_conexion(datetime(2025, 4, 15, 10, 40, 21))
        'Fecha de último acceso desconocida'

        >>> alumno = {"ID": 2, "Alumno": "Amy Wong", "Correo": "amy@marsuniversity.edu", "UltimoAcceso": "2 days"}
        >>> controlador = ControladorDatos(alumno)
        >>> controlador.calculo_ultima_conexion(datetime(2025, 4, 15, 10, 40, 21))
        'Formato de último acceso incorrecto'

        >>> alumno = {"ID": 3, "Alumno": "Turanga Leela", "Correo": "leela@planetexpress.com", "UltimoAcceso": "10 minutos 20 segundos"}
        >>> controlador = ControladorDatos(alumno)
        >>> controlador.calculo_ultima_conexion(datetime(2025, 4, 15, 10, 40, 21))
        '15-04-2025 10:30:01'

        >>> alumno = {"ID": 4, "Alumno": "Bender Rodríguez", "Correo": "bender@ilovekillinghumans.com", "UltimoAcceso": "5 segundos"}
        >>> controlador = ControladorDatos(alumno)
        >>> controlador.calculo_ultima_conexion(datetime(2025, 4, 15, 10, 40, 21))
        '15-04-2025 10:40:16'

        >>> alumno = {"ID": 5, "Alumno": "Professor Farnsworth", "Correo": "prof.farnsworth@planetexpress.com", "UltimoAcceso": "11 días 22 horas 12 minutos 10 segundos"}
        >>> controlador = ControladorDatos(alumno)
        >>> controlador.calculo_ultima_conexion(datetime(2025, 4, 15, 10, 40, 21))
        '03-04-2025 12:28:11'
        """

        dias = 0
        horas = 0
        minutos = 0
        segundos = 0

        # Cambiar self.alumno[3] por self.alumno["UltimoAcceso"]
        ultimo_acceso = self.alumno.get("UltimoAcceso", "")

        if ultimo_acceso == "":
            return "Fecha de último acceso desconocida"
        else:
            acceso_split = ultimo_acceso.split()
            for i in range(0, len(acceso_split), 1):
                if acceso_split[i] == "días":
                    dias = int(acceso_split[i - 1])

                elif acceso_split[i] == "horas":
                    horas = int(acceso_split[i - 1])

                elif acceso_split[i] == "minutos":
                    minutos = int(acceso_split[i - 1])

                elif acceso_split[i] == "segundos":
                    segundos = int(acceso_split[i - 1])

            if dias == 0 and horas == 0 and minutos == 0 and segundos == 0:
                return "Formato de último acceso incorrecto"
            else:
                ultimo_acceso = timedelta(
                    days=dias, hours=horas, minutes=minutos, seconds=segundos
                )
                fecha_hora_ultimo_acceso = fecha_hora_actual - ultimo_acceso
                fecha_hora_ultimo_acceso_formateada = fecha_hora_ultimo_acceso.strftime(
                    "%d-%m-%Y %H:%M:%S"
                )
                return fecha_hora_ultimo_acceso_formateada
