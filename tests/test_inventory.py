from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_inventory(login_in_driver, hay_productos_visibles, hay_menu, hay_filtros, obtener_primer_producto):
    try:
        driver = login_in_driver

        # Verificamos que el titulo de la pagina sea correcto
        assert driver.title == "Swag Labs", "El titulo de la pagina no es correcto"

        # Capturamos todos los productos de la pagina y validamos que la lista no este vacia
        assert hay_productos_visibles, "No hay productos visibles en el inventario"

        # time.sleep(2)

        # Validar elementos importantes de la interfaz (menu y filtros)
        assert hay_menu, "No hay un menu en la pagina"
        assert hay_filtros, "No hay filtros de busqueda en la pagina"

        # Validar nombre y precio del primer producto
        primer_producto = obtener_primer_producto
        print(f"Primer producto → {primer_producto["nombre"]} - {primer_producto["precio"]}")

        time.sleep(2)

    except Exception as e:
        print(f"Error en test_inventory: {e}")
        raise 

    finally:
        driver.quit()

