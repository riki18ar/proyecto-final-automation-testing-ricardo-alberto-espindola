from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Clase que representa la página de inventario con las constanstes URL, Menu hamburguesa, botón de cierre de sesión, botón "Add to cart" y enlace del carrito de compras.
class InventoryPage:
    URL_CURRENT = "/inventory.html"
    MENU_BUTTON_ID = (By.ID, "react-burger-menu-btn")
    LINK_LOGOUT_ID = (By.ID, "logout_sidebar_link")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    # Constructor de la clase InventoryPage.
    def __init__(self, driver):
        self.driver = driver
    # Función para verificar si estamos en la página de inventario.
    def is_at_page(self):
        return self.URL_CURRENT in self.driver.current_url
    # Funcion para agregar un producto al carrito de compras.
    def add_product_to_cart(self, product_index=0):
        add_buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTON)
        if add_buttons and product_index < len(add_buttons):
            add_buttons[product_index].click()
    # Funcion para ir al carrito de compras.
    def go_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CART_LINK)
        ).click()
    # Funcion para cerrar sesión.
    def logout( self ):
        self.driver.find_element(*self.MENU_BUTTON).click()
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LINK_BUTTON)
        ).click()