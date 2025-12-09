import pytest
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
from page.checkout_page import CheckoutPage 
import time

def test_checkout_process(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    # Paso 1: Iniciar sesión con un usuario válido.
    login.open()
    login.login("standard_user", "secret_sauce")
    time.sleep(3)
    # Paso 2: Agregar un producto al carrito y proceder al checkout.
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()
    time.sleep(3)
    cart.go_to_checkout()
    time.sleep(3)
    # Verificar que estamos en la página de checkout.
    assert checkout.is_at_page(), "No se está en la página de checkout."
    # Paso 3: Completar la información del cliente (nombre, apellido, zip code) y continuar al overview.
    checkout.fill_customer_info("Peter", "Pan", "31650")
    time.sleep(2)
    checkout.continue_to_overview()
    time.sleep(2)
    # Verificar que avanzamos a la página de overview del checkout.
    assert "checkout-step-two" in driver.current_url, "No se avanzó a la página de overview del checkout."

def test_checkout_validation(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    # Paso 1: Iniciar sesión con un usuario válido.
    login.open()
    login.login("standard_user","secret_sauce")
    time.sleep(3)
    # Paso 2: Agregar un producto al carrito y proceder al checkout.
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()
    cart.go_to_checkout()
    checkout.continue_to_overview()
    time.sleep(2)
    error_message = checkout.get_error_message()
    assert "First Name is required" in error_message