from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    # Contiene los selectores y constantes relacionados con la página del carrito de compras.
    URL_CURRENT = "/cart.html"
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    REMOVE_BUTTON = (By.XPATH, "//button[contains(text(), 'Remove')]")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    # Funcion inicializadora de los atributos la clase CartPage. 
    def __init__(self, driver):
        self.driver = driver
    # Funcion que verifica si estamos en la página del carrito de compras.
    def is_at_page(self):
        return self.URL_CURRENT in self.driver.current_url
    # Funcion que hace click en el boton de checkout.
    def go_to_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()
    # Funcion que hace click en el boton de continuar comprando.
    def continue_shopping(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONTINUE_SHOPPING_BUTTON)
        ).click()
    # Funcion que obtiene la cantidad de items en el carrito.
    def get_cart_items_count(self):
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)
    # Funcion que elimina un item del carrito por su indice.   
    def remove_item(self, item_index=0):
        remove_buttons = self.driver.find_elements(*self.REMOVE_BUTTON)
        if remove_buttons and item_index < len(remove_buttons):
            remove_buttons[item_index].click()
    # Funcion que obtiene la cantidad del badge del carrito.
    def get_cart_badge_count(self):
        try:
            badge = self.driver.find_element(*self.CART_BADGE)
            return int(badge.text)
        except:
            return 0