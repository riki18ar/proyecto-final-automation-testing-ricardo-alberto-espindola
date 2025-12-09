import pytest
from page.login_page import LoginPage
from data.data_login import CASOS_LOGIN
from utils.example_csv import get_login_csv 
from utils.faker import get_login_faker 


@pytest.mark.parametrize("username,password,login_bool", CASOS_LOGIN())
def test_valid_login(driver, username, password, login_bool):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)

    if login_bool:
        # Verifica que la URL actual contiene "inventory.html" después de un login exitoso.
        assert "inventory.html" in driver.current_url
    else:
        # Verifica que la URL actual no contiene "inventory.html" después de un login fallido.
        assert "inventory.html" not in driver.current_url