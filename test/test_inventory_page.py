from page.login_page import LoginPage
from page.inventory_page import InventoryPage
import time

def test_login_inventory_page(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    login_page.open()
    login_page.login()

    time.sleep(3)

    inventory_page.is_at_page()

    inventory_page.logout()
    time.sleep(3)
    assert "https://www.saucedemo.com/" in driver.current_url