import re
from datetime import datetime, timedelta


def transformar_a_segundos_desde_csv(dato: str, hora_actual: datetime) -> int:
    """
    Transforma una cadena con un formato de tiempo relativo a segundos desde la fecha y hora actual.

    Analiza una cadena de texto que representa un periodo de tiempo en días, horas, minutos y segundos
    y calcula el número de segundos transcurridos desde la fecha y hora actual. Si la cadena no tiene
    datos válidos o está vacía, devuelve 0.

    Args:
        dato (str): Cadena de texto con el tiempo relativo en días, horas, minutos y segundos.
                    Ejemplo: "2 días 3 horas 10 minutos 5 segundos".
        hora_actual (datetime): La fecha y hora actual para calcular la diferencia.

    Returns:
        int: El número de segundos desde la fecha y hora actual, calculado a partir de la cadena de texto.
             Devuelve 0 si la cadena no es válida o no contiene información de tiempo.

    Examples:
        >>> hora_actual = datetime(2025, 4, 15, 10, 40, 21)
        >>> transformar_a_segundos_desde_csv("2 días 3 horas 10 minutos 5 segundos", hora_actual)
        1681553901

        >>> transformar_a_segundos_desde_csv("5 horas 30 minutos", hora_actual)
        1681570801
    """
    if not dato or not isinstance(dato, str):
        return 0

    dias = horas = minutos = segundos = 0

    patrones = {
        "días": r"(\d+)\s*d[ií]as?",
        "horas": r"(\d+)\s*horas?",
        "minutos": r"(\d+)\s*minutos?",
        "segundos": r"(\d+)\s*segundos?",
    }

    for clave, patron in patrones.items():
        match = re.search(patron, dato, flags=re.IGNORECASE)
        if match:
            valor = int(match.group(1))
            if clave == "días":
                dias = valor
            elif clave == "horas":
                horas = valor
            elif clave == "minutos":
                minutos = valor
            elif clave == "segundos":
                segundos = valor

    diferencia = timedelta(days=dias, hours=horas, minutes=minutos, seconds=segundos)
    fecha_resultante = hora_actual - diferencia
    return int(fecha_resultante.timestamp())


def transformar_segundos_a_fecha(segundos: int) -> str:
    """
    Convierte una cantidad de segundos a un formato de fecha y hora.

    Dado un número de segundos desde la época (1970-01-01 00:00:00 UTC), devuelve
    la fecha y hora correspondiente en formato "YYYY-MM-DD HH:MM:SS".

    Args:
        segundos (int): Número de segundos desde la época.

    Returns:
        str: La fecha y hora correspondiente al número de segundos, en formato "YYYY-MM-DD HH:MM:SS".
             Si ocurre un error al convertir los segundos, devuelve una cadena vacía.

    Examples:
        >>> transformar_segundos_a_fecha(1681553901)
        '2025-04-15 10:40:01'

        >>> transformar_segundos_a_fecha(0)
        '1970-01-01 00:00:00'
    """
    try:
        fecha = datetime.fromtimestamp(segundos)
        return fecha.strftime("%Y-%m-%d %H:%M:%S")
    except (OSError, OverflowError, ValueError):
        return ""


def transformar_a_segundos(fecha: datetime) -> int:
    """
    Convierte una fecha y hora a segundos desde la época (1970-01-01 00:00:00 UTC).

    Args:
        fecha (datetime): Fecha y hora a convertir.

    Returns:
        int: El número de segundos transcurridos desde la época hasta la fecha dada.

    Examples:
        >>> transformar_a_segundos(datetime(2025, 4, 15, 10, 40, 21))
        1681554001

        >>> transformar_a_segundos(datetime(1970, 1, 1, 0, 0, 0))
        0
    """
    return int(fecha.timestamp())


def calcular_diferencia_tiempo(fecha1_str: str, fecha2_str: str) -> str:
    """
    Calcula la diferencia entre dos fechas y devuelve una cadena con el tiempo transcurrido.

    Dada dos fechas en formato "YYYY-MM-DD HH:MM:SS", calcula la diferencia en términos de días,
    horas, minutos y segundos, y devuelve una cadena que describe cuánto tiempo ha pasado
    entre ellas.

    Args:
        fecha1_str (str): La primera fecha en formato "YYYY-MM-DD HH:MM:SS".
        fecha2_str (str): La segunda fecha en formato "YYYY-MM-DD HH:MM:SS".

    Returns:
        str: La diferencia entre las dos fechas en formato "Hace X días, Y horas, Z min, W seg".
             Si las fechas son iguales, devuelve "Hace menos de un segundo".

    Examples:
        >>> calcular_diferencia_tiempo("2025-04-15 10:40:21", "2025-04-14 10:40:21")
        'Hace 1 días'

        >>> calcular_diferencia_tiempo("2025-04-15 10:40:21", "2025-04-14 09:40:21")
        'Hace 1 días, 1 horas'

        >>> calcular_diferencia_tiempo("2025-04-15 10:40:21", "2025-04-15 10:40:22")
        'Hace menos de un segundo'
    """
    formato = "%Y-%m-%d %H:%M:%S"
    fecha1 = datetime.strptime(fecha1_str, formato)
    fecha2 = datetime.strptime(fecha2_str, formato)

    diferencia = fecha1 - fecha2
    total_segundos = int(diferencia.total_seconds())

    dias = total_segundos // 86400
    horas = (total_segundos % 86400) // 3600
    minutos = (total_segundos % 3600) // 60
    segundos = total_segundos % 60

    partes = []
    if dias:
        partes.append(f"{dias} días")
    if horas:
        partes.append(f"{horas} horas")
    if minutos:
        partes.append(f"{minutos} min")
    if segundos:
        partes.append(f"{segundos} seg")

    return "Hace " + ", ".join(partes) if partes else "Hace menos de un segundo"


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
