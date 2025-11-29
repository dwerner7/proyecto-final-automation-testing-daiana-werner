from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from utils.logger import logger

class InventoryPage:
    # Selectores
    _INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    _ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    
    _ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn_inventory")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    _CART_COUNT = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self,driver):
        self.driver = driver 
        self.wait = WebDriverWait(driver,10)

    def obtener_todos_los_productos(self):
        # Espera a que todos los elementos esten presentes
        self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEMS))
        # Toma los elementos y arma una lista con ellos (*)
        productos = self.driver.find_elements(*self._INVENTORY_ITEMS)
        return productos

    def obtener_nombres_productos(self):
        productos = self.driver.find_elements(*self._ITEM_NAME)
        return [producto_nombre.text for producto_nombre in productos]
    # Recorre la lista de nombres (productos) y en cada iteracion guardamos el nombre convertido en texto

    def agregar_primer_producto(self):
        # productos = self.wait.until(EC.visibility_of_all_elements_located(*self._INVENTORY_ITEMS))
        productos = self.obtener_todos_los_productos()
                    
        primer_boton_producto = productos[0].find_element(*self._ADD_TO_CART_BUTTON)
        primer_boton_producto.click()

    def agregar_producto_por_nombre(self,nombre_producto):
        # productos = self.obtener_todos_los_productos()

        productos = self.driver.find_elements(*self._INVENTORY_ITEMS)

        for producto in productos:
            nombre = producto.find_element(*self._ITEM_NAME).text

            if nombre.strip() == nombre_producto.strip(): # .lower() ???
                boton = producto.find_element(self._ADD_TO_CART_BUTTON)
                boton.click()
            else:
                raise Exception(f"No se encontro el producto {nombre_producto}")

    def abrir_carrito(self):
        self.wait.until(EC.element_to_be_clickable(self._CART_LINK)).click()

    def obtener_conteo_carrito(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self._CART_COUNT))
            contador_carrito = self.driver.find_element(self._CART_COUNT)
            return int(contador_carrito.text)
        except:
            return 0
