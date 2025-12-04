from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import logger

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_inventory(login_in_driver,usuario,password):
    logger.info("Iniciando test de inventario...")
    try:

        driver = login_in_driver
        LoginPage(driver).login_completo(usuario,password)

        inventory_page = InventoryPage(driver)

        # Verificar que hay productos
        productos = inventory_page.obtener_todos_los_productos()
        logger.info(f"Cantidad de productos presentes en el inventario: {len(productos)}")
        assert len(productos) > 0, "El inventario esta vacio"

        # Verificar que el carrito se encuentre vacio al inicio
        logger.info(f"Cantidad de productos en el carrito: {inventory_page.obtener_conteo_carrito()}")
        assert inventory_page.obtener_conteo_carrito() == 0

        # Agregar el primer producto al carrito
        inventory_page.agregar_primer_producto()
        logger.info("1 producto agregado al carrito")

        # Verificar el contador del carrito
        logger.info(f"Cantidad actualizada de productos en el carrito: {inventory_page.obtener_conteo_carrito()}")
        assert inventory_page.obtener_conteo_carrito() == 1

        logger.info("Test de inventario completo")

    except Exception as e:
        print(f"Error en test_inventory: {e}")
        logger.info(f"Error en test de inventario - {e}")
        raise
    
    logger.info("_______________________________________________________________________________")
