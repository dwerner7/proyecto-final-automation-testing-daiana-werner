import pytest

# Lista de archivos de las pruebas a ejecutar
test_files = [
    "tests/test_login.py",
    "tests/test_login_faker.py",
    "tests/test_inventory.py",
    "tests/test_cart.py",
    "tests/test_cart_json.py",
    "tests/test_api.py"
]

# pytest argumentos para ejecutar las pruebas: archivos + reporte HTML
pytest_args = test_files + [
    "--html=report.html",
    "--self-contained-html", 
    "-v"
]

pytest.main(pytest_args)