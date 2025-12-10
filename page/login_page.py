from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import URL
from selenium.webdriver.common.by import By

# Clase que representa la página de login.
class LoginPage:
    _INPUT_NAME_FIELD = (By.NAME ,"user-name")
    _INPUT_PASSWORD_FIELD = (By.NAME ,"password")
    _LOGIN_BUTTON = (By.NAME, "login-button")
    #_LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")
    def __init__(self, driver):
        self.driver = driver
    # Función para abrir la página de login.
    def open(self):
        self.driver.get(URL)
    # Función para realizar el inicio de sesión con las credenciales proporcionadas.
    def login(self, username , password ):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self._INPUT_NAME_FIELD)
            ).send_keys(username)
    # Función para ingresar la contraseña y hacer clic en el botón de inicio de sesión.
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self._INPUT_PASSWORD_FIELD)
            ).send_keys(password)
    # Función para hacer clic en el botón de inicio de sesión.
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self._LOGIN_BUTTON)
            ).click()