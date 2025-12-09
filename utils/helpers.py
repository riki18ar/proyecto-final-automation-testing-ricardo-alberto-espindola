from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager    
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import os
# Configuración del driver de Selenium para Chrome
CHROME_BINARY_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
URL = "https://www.saucedemo.com/"

# Función para inicializar y obtener el driver de Selenium con las opciones configuradas.
def get_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = CHROME_BINARY_PATH
    prefs = {
        # Evita que aparezca el popup de guardar contraseñas
        "credentials_enable_service": False,
        # Desactiva la gestión de contraseñas segura del navegador.
        "profile.password_manager_leak_detection": False,
    }
    chrome_options.add_experimental_option("prefs", prefs)  
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(5)
    return driver

def get_file_path(file_name,folder="data"):
    
    current_file = os.path.dirname(__file__)
    file_path = os.path.join(current_file, "..", folder, file_name)
    return os.path.abspath(file_path)