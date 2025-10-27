from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_cart(login_in_driver, obtener_primer_producto, agregar_un_producto_al_carrito, obtener_producto_del_carrito):
    try:
        driver = login_in_driver
        
        primer_producto = obtener_primer_producto
       
        time.sleep(5)

       # Verificar que el contador del carrito este en 1 al agregar un producto
        assert agregar_un_producto_al_carrito, "El contador del carrito es incorrecto (se esperaba 1)"

        time.sleep(2)

        # Validar que el producto añadido aparezca correctamente en el carrito
        assert obtener_producto_del_carrito["nombre"] == primer_producto["nombre"], "El producto del carrito no coincide"

        # time.sleep(2)

    except Exception as e:
        print(f"Error en test_cart: {e}")
        raise 

    finally:
        driver.quit()