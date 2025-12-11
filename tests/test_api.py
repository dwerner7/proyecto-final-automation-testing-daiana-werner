import requests
import pytest
from utils.logger import logger
from pages.api_page import APIPage

# Obtener usuario
@pytest.mark.parametrize("id_usuario",[2])
def test_get_user(id_usuario):
    api = APIPage()

    logger.info(f"Realizando la solicitud GET a {api._URL_BASE} del usuario con id {id_usuario}")
    response = api.get_user(id_usuario)

    logger.info(f"Status code: {response.status_code}")
    assert response.status_code == 200, f"Error al obtener el usuario con id {id_usuario}"

    data = response.json()

    print(data)
    
    logger.info(f"ID del usuario obtenido: {data["id"]}")
    assert data["id"] == id_usuario

    logger.info("_______________________________________________________________________________")


# Crear usuario
@pytest.mark.parametrize("payload",[{
        "name": "Pepe",
        "website": "zapateriapepe.com"
    }])
def test_create_user(payload):
    api = APIPage()

    logger.info(f"Realizando la solicitud POST a {api._URL_BASE} de un nuevo usuario: {payload["name"]} - {payload["website"]}")
    response = api.create_user(payload)

    logger.info(f"Status code: {response.status_code}")
    assert response.status_code == 201, "Error al crear el usuario"

    data = response.json()

    logger.info(f"Nombre del usuario creado: {data["name"]}")
    assert data["name"] == payload["name"]

    logger.info("_______________________________________________________________________________")


# Eliminar usuario
@pytest.mark.parametrize("id_usuario",["1"])
def test_delete_user(id_usuario):
    api = APIPage()

    logger.info(f"Realizando la solicitud DELETE a {api._URL_BASE} del usuario con id {id_usuario}")
    response = api.delete_user(id_usuario)

    logger.info(f"Status code: {response.status_code}")
    assert response.status_code == 200, f"Error al eliminar al usuario con id {id_usuario}"

    data = response.json()

    logger.info(f"Respuesta de la API: {data}")
    # La API nos devuelve un json vacio
    assert len(data) == 0

    logger.info("_______________________________________________________________________________")

# ----------------------------- Encadenamiento de peticiones ------------------------------------------
@pytest.mark.skip(reason="problemas de la api con el id")
# Lo comento porque la API no encuentra al usuario que creé buscándolo con su id, trae a otro usuario por lo que los tests fallan
@pytest.mark.parametrize("payload",[{
        "name": "Maria",
        "website": "floreriafresia.com"
    }])
def test_crear_y_obtener_user(payload):
    api = APIPage()

    logger.info(f"Realizando la solicitud POST a {api._URL_BASE} de un nuevo usuario: {payload["name"]} - {payload["website"]}")
    # Creamos el nuevo usuario
    response_crear_usuario = api.create_user(payload)

    logger.info(f"Status code: {response_crear_usuario.status_code}")
    assert response_crear_usuario.status_code == 201, "Error al crear el usuario"

    # Obtenemos la data y extraemos el id
    usuario_creado = response_crear_usuario.json()
    id_usuario = usuario_creado["id"]

    logger.info(f"Usuario creado con id: {id_usuario}")

    # Con el id buscamos al usuario creado
    logger.info(f"Realizando la solicitud GET a {api._URL_BASE} del usuario con id {id_usuario}")
    response_obtener_usuario = api.get_user(id_usuario)

    logger.info(f"Status code: {response_obtener_usuario.status_code}")
    assert response_obtener_usuario.status_code == 200, f"Error al obtener el usuario con id {id_usuario}"

    # Validamos que los datos del usuario obtenido son correctos
    usuario_obtenido = response_obtener_usuario.json()
    
    assert usuario_obtenido["name"] == payload["name"]
    assert usuario_obtenido["website"] == payload["website"]
    logger.info(f"Usuario obtenido: {payload["name"]} - {payload["website"]}")

