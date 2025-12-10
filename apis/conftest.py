import pytest
import logging
import pathlib

@pytest.fixture(scope="session")

# Función que proporciona la URL base para las pruebas de API.
def api_url():
    return "https://jsonplaceholder.typicode.com"  # URL base para las peticiones HTTP de prueba
# Configuración del logger para registrar eventos durante las pruebas.
path_dir = pathlib.Path('logs')
# Crear el directorio si no existe
path_dir.mkdir(exist_ok=True)
# Configuración básica del logger
logging.basicConfig(
    filename = path_dir/ 'historial.log',
    level= logging.INFO,
    format= '%(asctime)s - %(levelname)s - %(message)s',
    datefmt= '%H:%M:%S')
logger = logging.getLogger()