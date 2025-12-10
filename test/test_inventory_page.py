from page.login_page import LoginPage
from page.inventory_page import InventoryPage
import time

# Función de prueba para verificar el inicio de sesión y la página de inventario.
def test_login_inventory_page(driver):
    # Genera una instancia de las páginas de Login e Inventario.
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    login_page.open()
    # Inserta las credenciales válidas para realizar el inicio de sesión.
    login_page.login("standard_user", "secret_sauce")
    time.sleep(2)
    inventory_page.is_at_page()
    inventory_page.logout()
    time.sleep(3)
    # Verificar que se ha cerrado sesión correctamente.
    assert "https://www.saucedemo.com/" in driver.current_url