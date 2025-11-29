import requests
import pytest
from utils.logger import logger
from pages.api_page import APIPage

# Obtener usuario
@pytest.mark.parametrize("id_usuario",[2])
def test_get_user(id_usuario):
    api = APIPage()

    logger.info(f"Realizando la solicitud GET a {api._URL_BASE} del usuario con id {id_usuario}")
    
    # response = requests.get(f"{url_base}/{id_usuario}",headers=header_request)
    response = api.get_user(id_usuario)

    logger.info(f"Status code: {response.status_code}")
    assert response.status_code == 200, f"Error al obtener el usuario con id {id_usuario}"

    data = response.json()
    
    logger.info("Validando el id dentro del usuario")
    assert data["data"]["id"] == id_usuario


# Crear usuario
@pytest.mark.parametrize("payload",[{
        "name": "Jose",
        "job": "Profesor"
    }])
def test_create_user(payload):
    api = APIPage()

    logger.info(f"Realizando la solicitud POST a {api._URL_BASE} de un nuevo usuario con nombre {payload["name"]} y profesion {payload["job"]}")
    # response = requests.post(url_base,headers=header_request,json=payload)

    response = api.create_user(payload)

    logger.info(f"Status code: {response.status_code}")
    assert response.status_code == 201, "Error al crear el usuario"

    data = response.json()

    logger.info("Validando el nombre dentro del usuario")
    assert data["name"] == payload["name"]


# Eliminar usuario
@pytest.mark.parametrize("id_usuario",["2"])
def test_delete_user(id_usuario):
    api = APIPage()

    logger.info(f"Realizando la solicitud DELETE a {api._URL_BASE} del usuario con id {id_usuario}")
    
    # response = requests.delete(f"{url_base}/{id_usuario}",headers=header_request)

    response = api.delete_user(id_usuario)

    logger.info(f"Status code: {response.status_code}")
    assert response.status_code == 204, f"Error al eliminar al usuario con id {id_usuario}"

    data = response.json()

    logger.info("Validando que el json de respuesta este vacio")
    assert len(data) == 0


# Encadenamiento de peticiones
@pytest.mark.parametrize("payload",[{
        "name": "Pepe",
        "job": "Zapatero"
    }])
def test_crear_y_obtener_user(payload):
    api = APIPage()

    logger.info(f"Realizando la solicitud POST a {api._URL_BASE} de un nuevo usuario: {payload["name"]} - {payload["job"]}")
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
    assert usuario_obtenido["job"] == payload["job"]
    logger.info(f"Usuario obtenido: {payload["name"]} - {payload["job"]}")

