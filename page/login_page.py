from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import URL
from selenium.webdriver.common.by import By

class LoginPage:
    _INPUT_NAME_FIELD = (By.NAME ,"user-name")
    _INPUT_PASSWORD_FIELD = (By.NAME ,"password")
    _LOGIN_BUTTON = (By.NAME, "login-button")
    #_LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")
    def __init__(self, driver):
        self.driver = driver
    
    def open(self):
        self.driver.get(URL)
    
    def login(self, username , password ):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self._INPUT_NAME_FIELD)
            ).send_keys(username)
        
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self._INPUT_PASSWORD_FIELD)
            ).send_keys(password)
        
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self._LOGIN_BUTTON)
            ).click()
        