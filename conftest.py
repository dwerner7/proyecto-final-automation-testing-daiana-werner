import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options

import pathlib
from datetime import datetime

# Directorio donde se van a almacenar las capturas de pantalla
target =  pathlib.Path("reports/screens")
target.mkdir(parents=True, exist_ok=True) 

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def login_in_driver(driver,usuario,password):
    LoginPage(driver).abrir_pagina()
    return driver

# -----------------CAPTURAS DE PANTALLA  ---------------------

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call): 
    outcome = yield 
    report = outcome.get_result()

    if report.when in ("setup","call") and report.failed:
        driver = item.funcargs.get("driver",None)

        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = target / f"{report.when}_{item.name}_{timestamp}.png"
            driver.save_screenshot(str(file_name))

# ------------------------------ API ------------------------------

# @pytest.fixture
# def url_base():
#     return "https://reqres.in/api/users"

# @pytest.fixture
# def header_request():
#     return {"x-api-key": "reqres-free-v1"}
