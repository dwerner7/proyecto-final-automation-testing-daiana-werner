import pytest
from selenium import webdriver
from utils import login, has_visible_products, has_menu, has_filters, get_first_item_info, correct_inventory_title, add_to_cart_and_increment_one, get_item_in_cart

@pytest.fixture
def driver():
    # --- Evita que aparezca la ventana del Gestor de contraseñas de Google ---
    # Creamos opciones para el Chrome
    options = webdriver.ChromeOptions()

    # Sesion en modo incognito, impide pop-up de contraseña insegura
    options.add_argument("--incognito")

    # Definimos navegador con opciones cargadas
    driver = webdriver.Chrome(options=options)
    # -------------------------------------------------------------------------

    yield driver
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver

#--------------------------------------------------------

@pytest.fixture
def hay_productos_visibles(driver):
    return has_visible_products(driver)

@pytest.fixture
def hay_menu(driver):
    return has_menu(driver)

@pytest.fixture
def hay_filtros(driver):
    return has_filters(driver)

@pytest.fixture
def obtener_primer_producto(driver):
    return get_first_item_info(driver)

@pytest.fixture
def titulo_inventario_correcto(driver):
    return correct_inventory_title(driver)

@pytest.fixture
def agregar_un_producto_al_carrito(driver):
    return add_to_cart_and_increment_one(driver)

@pytest.fixture
def obtener_producto_del_carrito(driver):
    return get_item_in_cart(driver)