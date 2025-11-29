from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest 

from pages.login_page import LoginPage
from utils.logger import logger

from faker import Faker

# Inicializamos Faker
fake = Faker()

@pytest.mark.parametrize("usuario,password,debe_funcionar", [
    (fake.user_name(), fake.password(length=8,special_chars=True,upper_case=True,lower_case=True,digits=True), False),
    (fake.user_name(), fake.password(), False)
])
def test_login_validation(login_in_driver,usuario,password,debe_funcionar):
    logger.info("Iniciando test login con faker utilizando credenciales inválidas...")
    logger.info(f"Completando con los datos de usuario: '{usuario} - {password}'")

    driver = login_in_driver
    if debe_funcionar:
        logger.info("Verificando redireccionamiento dentro de la pagina")
        
        assert "/inventory.html" in driver.current_url, "No se redirgio al inventario"
        
        logger.info(f"Test de login de usuario {usuario} exitoso")
    
    elif debe_funcionar == False:
        mensaje_error = LoginPage(driver).obtener_error()
        logger.info(f"Error en test de login - {mensaje_error}")
        assert "Epic sadface" in mensaje_error, "el mensaje de error no se esta mostrando"


