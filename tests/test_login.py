from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_validation(login_in_driver, titulo_inventario_correcto):
    try:
        driver = login_in_driver

        # Validar redireccion al inventario
        assert "/inventory.html" in driver.current_url, "No se redirige correctamente al inventario"

        # Validar título de la página de inventario
        assert titulo_inventario_correcto, f"El Titulo deberia ser 'Products'"

    except Exception as e:
        print(f"Error en test_login: {e}")
        raise 
    
    finally:
        driver.quit()

