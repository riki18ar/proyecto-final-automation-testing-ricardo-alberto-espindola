import pytest
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
from page.checkout_page import CheckoutPage 
from page.checkout_complete_page import CheckoutCompletePage 
import time

def test_checkout_purchase_flow(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    complete = CheckoutCompletePage(driver)
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
    checkout.fill_customer_information("Peter", "Pan", "31650")
    time.sleep(2)
    checkout.continue_to_overview()
    time.sleep(2)
    driver.get("https://www.saucedemo.com/checkout-complete.html")
    # Verificar que avanzamos a la página de overview del checkout.
    assert complete.is_at_page(), "No se está en la página de checkout complete."
    assert "THANK YOU FOR YOUR ORDER" in complete.get_success_message(), "El mensaje de éxito no es correcto."
    assert complete.is_success_image_displayed(), "La imagen de éxito no se muestra correctamente."
    # Paso 4: Regresar a la página de inventario.
    complete.back_to_home()
    time.sleep(2)
    assert inventory.is_at_page(), "No se regresó a la página de inventario."
