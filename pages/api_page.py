import requests
import pytest
from utils.logger import logger

class APIPage:
    _URL_BASE = "https://jsonplaceholder.typicode.com/users"
    # _HEADER_REQUEST = {"x-api-key": "reqres-free-v1"}

    def get_user(self,user_id):
        response = requests.get(f"{self._URL_BASE}/{user_id}")
        return response

    def create_user(self,payload):
        response = requests.post(self._URL_BASE,json=payload)
        return response

    def delete_user(self,user_id):
        response = requests.delete(f"{self._URL_BASE}/{user_id}")
        return response
