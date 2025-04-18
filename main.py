"""Módulo principal de la aplicación.

Este módulo maneja la ejecución principal de la aplicación, incluyendo:
- La inicialización de la interfaz gráfica (PySide6/Qt)
- La gestión de argumentos de línea de comandos
- La ejecución de pruebas doctest cuando se solicita

Ejemplo de uso:
    python main.py              # Ejecuta la aplicación normalmente
    python main.py --test       # Ejecuta pruebas doctest
"""

import sys
import doctest
from PySide6.QtWidgets import QApplication
from controller import controller_datos
from controller.controller_conection import ControladorConexion


if __name__ == "__main__":
    """Punto de entrada principal de la aplicación.

    Configura la aplicación Qt y decide entre:
    - Modo prueba (--test): Ejecuta pruebas doctest en controller_datos
    - Modo normal: Inicia la interfaz gráfica principal

    El sistema sale con código:
    - 0 si la ejecución fue exitosa
    - 1 si hubo errores (manejado por Qt/PySide6)
    """
    app = QApplication(sys.argv)

    if "--test" in sys.argv:
        # Ejecuta pruebas doctest en el módulo controller_datos
        resultado = doctest.testmod(controller_datos, verbose=True)

    else:
        # Inicia la interfaz gráfica principal
        ventana = ControladorConexion()
        ventana.show()
        sys.exit(app.exec())
