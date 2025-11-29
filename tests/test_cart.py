from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.logger import logger

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_cart(login_in_driver,usuario,password):
    logger.info("Iniciando test de carrito...")
    try:
        
        driver = login_in_driver
        inventory_page = InventoryPage(driver)

        # Agregar el producto al carrito 
        inventory_page.agregar_primer_producto()

        logger.info("Agregando 1 producto al carrito")

        # Abrir el carrito
        inventory_page.abrir_carrito()

        # Validar que haya un producto en el carrito
        cart_page = CartPage(driver)

        productos_en_carrito = cart_page.obtener_nombre_producto_carrito()
        logger.info(f"Cantidad de productos en el carrito: {len(productos_en_carrito)}")
        assert len(productos_en_carrito) == 1

        logger.info("Test de carrito completo")

    except Exception as e:
        print(f"Error en test_cart: {e}")
        logger.info(f"Error en test de carrito --> {e}")
        raise
    finally:
        driver.quit()