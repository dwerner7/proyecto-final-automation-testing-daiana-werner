from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import time

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.lector_json import leer_json_productos
from utils.logger import logger

RUTA_JSON = "datos/productos.json"

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
@pytest.mark.parametrize("nombre_producto",leer_json_productos(RUTA_JSON))
def test_cart_json(login_in_driver,usuario,password,nombre_producto):
    logger.info("Iniciando test de inventario con productos tomados de un json...")
    try:
        logger.info(f"Producto: {nombre_producto}")

        driver = login_in_driver
        LoginPage(driver).login_completo(usuario,password)

        inventory_page = InventoryPage(driver)

        # Agregar al carrito el producto
        inventory_page.agregar_producto_por_nombre(nombre_producto)
        logger.info(f"Agregando producto '{nombre_producto}' al carrito")

        # Abrir el carrito
        inventory_page.abrir_carrito()

        time.sleep(2)

        # Validar que haya un producto en el carrito
        cart_page = CartPage(driver)

        logger.info(f"Nombre del producto en el carrito: {cart_page.obtener_nombre_producto_carrito()}")

        assert cart_page.obtener_nombre_producto_carrito() == nombre_producto

        logger.info("Test de carrito completo")

    except Exception as e:
        print(f"Error en test_cart: {e}")
        raise

    logger.info("_______________________________________________________________________________")