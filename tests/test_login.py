from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest 

from utils.lector_csv import leer_csv_login
from pages.login_page import LoginPage

from utils.logger import logger

@pytest.mark.parametrize("usuario,password,debe_funcionar",leer_csv_login("datos/data_login.csv"))
def test_login_validation(login_in_driver,usuario,password,debe_funcionar):
    logger.info("Iniciando test de login con datos de inicio de sesion externos (csv)...")
    logger.info(f"Completando con los datos de usuario: '{usuario} - {password}'")

    driver = login_in_driver
    LoginPage(driver).login_completo(usuario,password)

    if debe_funcionar:
        logger.info("Verificando redireccionamiento dentro de la pagina")
        
        assert "/inventory.html" in driver.current_url, "No se redirigio al inventario"
        
        logger.info(f"Test de login de usuario {usuario} exitoso")

    elif debe_funcionar == False:
        mensaje_error = LoginPage(driver).obtener_error()
        logger.info(f"Error en test de login - {mensaje_error}")
        assert "Epic sadface" in mensaje_error, "el mensaje de error no se esta mostrando"

    logger.info("_______________________________________________________________________________")
