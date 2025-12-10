import pytest
from page.login_page import LoginPage
from data.data_login import CASOS_LOGIN
from utils.example_csv_json import get_login_csv, get_login_json
from utils.faker import get_login_faker
import time 

# Parametrización de pruebas utilizando datos de CAS
@pytest.mark.parametrize("username,password,login_bool", CASOS_LOGIN)
def test_valid_login(driver, username, password, login_bool):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    time.sleep(1)
    if login_bool:
        # Verifica que la URL actual contiene "inventory.html" después de un login exitoso.
        assert "inventory.html" in driver.current_url
    else:
        # Verifica que la URL actual no contiene "inventory.html" después de un login fallido.
        assert "inventory.html" not in driver.current_url

# Parametrización de pruebas utilizando datos de un archivo CSV
@pytest.mark.parametrize("username,password,login_bool", get_login_csv())
def test_valid_login_csv(driver, username, password, login_bool):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    time.sleep(1)
    if login_bool:
        # Verifica que la URL actual contiene "inventory.html" después de un login exitoso.
        assert "inventory.html" in driver.current_url
    else:
        # Verifica que la URL actual no contiene "inventory.html" después de un login fallido.
        assert "inventory.html" not in driver.current_url

 # Parametrización de pruebas utilizando datos de un archivo Json
@pytest.mark.parametrize("username,password,login_bool", get_login_json())
def test_valid_login_json(driver, username, password, login_bool):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    time.sleep(1)
    if login_bool:
        # Verifica que la URL actual contiene "inventory.html" después de un login exitoso.
        assert "inventory.html" in driver.current_url
    else:
        # Verifica que la URL actual no contiene "inventory.html" después de un login fallido.
        assert "inventory.html" not in driver.current_url

# Parametrización de pruebas utilizando datos generados por Faker
@pytest.mark.parametrize("username,password,login_bool", get_login_faker())
def test_valid_login_faker(driver, username, password, login_bool):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    time.sleep(1)
    if login_bool:
        # Verifica que la URL actual contiene "inventory.html" después de un login exitoso.
        assert "inventory.html" in driver.current_url
    else:
        # Verifica que la URL actual no contiene "inventory.html" después de un login fallido.
        assert "inventory.html" not in driver.current_url