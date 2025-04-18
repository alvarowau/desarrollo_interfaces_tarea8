# TAREA8_DI

**TAREA8_DI** es una aplicación desarrollada en Python que utiliza una arquitectura modular para gestionar accesos de usuarios. El proyecto está organizado en varios módulos que separan la lógica de control, la interfaz de usuario, la gestión de datos y las utilidades.

## ¿Qué hace esta aplicación?

La aplicación se conecta a una tabla llamada `alumnos` con la siguiente estructura:

```sql
CREATE TABLE IF NOT EXISTS alumnos (
    ID INT PRIMARY KEY,
    Alumno VARCHAR(50),
    Correo VARCHAR(50),
    UltimoAcceso VARCHAR(50)
);
```

Si no se utiliza Docker, esta tabla debe crearse manualmente en la base de datos del usuario.

Al iniciar, se mostrará un selector de conexión donde se puede introducir la configuración de acceso a la base de datos local: host (localhost), puerto, nombre de base de datos, usuario y contraseña.

Una vez conectado, la aplicación:

- Muestra el contenido actual de la tabla `alumnos`.
- Permite cargar un archivo CSV (por ejemplo `Acceso.csv`) cuyos datos se insertan en la base de datos.
- Ofrece la opción de eliminar el contenido completo de la tabla.
- Muestra información del alumno, incluyendo su nombre, fecha de último acceso y la fecha actual.

## Estructura del Proyecto

- **controller/**: Contiene la lógica de control de la aplicación.
- **repository/**: Maneja la interacción con la base de datos.
- **ui/**: Define la interfaz de usuario.
- **util/**: Incluye funciones y utilidades auxiliares.
- **main.py**: Punto de entrada principal de la aplicación.
- **init.sql**: Script de inicialización para la base de datos.
- **Acceso.csv**: Archivo CSV utilizado para importar datos de acceso.
- **docker-compose.yml**: Configuración para ejecutar la aplicación en contenedores Docker.
- **requirements.txt**: Lista de dependencias necesarias para ejecutar la aplicación.
- **uso.webm**: Video demostrativo del funcionamiento de la aplicación.

## Requisitos Previos

- Python 3.8 o superior
- Docker y Docker Compose (opcional, para ejecución en contenedores)

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/alvarowau/desarrollo_interfaces_tarea8
   cd TAREA8_DI
   ```

2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta la aplicación:

   ```bash
   python main.py
   ```

## Uso con Docker

Para ejecutar la aplicación utilizando Docker:

```bash
docker-compose up
```

Esto iniciará los servicios definidos en `docker-compose.yml`, incluyendo la base de datos y la aplicación.

## Base de Datos

El script `init.sql` se utiliza para inicializar la base de datos con las tablas necesarias. Asegúrate de ejecutarlo en tu sistema de gestión de bases de datos antes de iniciar la aplicación, especialmente si no usas Docker.

## Video Demostrativo

Para ver una demostración del funcionamiento de la aplicación, consulta el archivo `uso.webm` incluido en el repositorio.

## Licencia

Este proyecto se distribuye bajo la Licencia MIT. Consulta el archivo `LICENSE` para más información.

