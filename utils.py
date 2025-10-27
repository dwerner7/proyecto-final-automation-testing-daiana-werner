from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login(driver):
    driver.get("https://www.saucedemo.com/")

    # Espera explicita
    wait = WebDriverWait(driver,10)

    driver.implicitly_wait(5)

    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

# ---------------------------------- PRODUCTOS ---------------------------------------------
def correct_inventory_title(driver):
    inventory_title = driver.find_element(By.CLASS_NAME, "title").text
    return inventory_title == "Products"

def has_visible_products(driver):
    wait = WebDriverWait(driver,10)
    products = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
    return len(products) > 0

def has_menu(driver):
    menus = driver.find_elements(By.ID,"react-burger-menu-btn")
    return len(menus) > 0

def has_filters(driver):
    filters = driver.find_elements(By.CLASS_NAME,"product_sort_container")
    return len(filters) > 0

def get_item_info(item):
    name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
    price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
    return {"nombre": name, "precio": price}
    return 

def get_first_item_info(driver):
    first_item = get_first_item(driver)
    return get_item_info(first_item)

def get_first_item(driver):
    return driver.find_element(By.CLASS_NAME, "inventory_item")


# ---------------------------------- CARRITO ---------------------------------------------
def add_to_cart_and_increment_one(driver):
    wait = WebDriverWait(driver,10)

    # Agrega producto al carrito
    item = get_first_item(driver)
    item.find_element(By.CLASS_NAME, "btn_inventory").click()
    
    time.sleep(2)

    # Cantidad de productos en el carrito
    cart_badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))).text
    return cart_badge == "1"

def get_in_the_cart_page(driver):
    # Accede al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

def get_item_in_cart(driver):
    get_in_the_cart_page(driver)

    # Obtengo el producto agregado al carrito
    item = driver.find_element(By.CLASS_NAME,"cart_item")
    # Devuelvo su nombre y precio
    return get_item_info(item)

