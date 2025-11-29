import requests
import pytest
from utils.logger import logger

class APIPage:
    _URL_BASE = "https://reqres.in/api/users"
    _HEADER_REQUEST = {"x-api-key": "reqres-free-v1"}

    def get_user(self,user_id):
        response = requests.get(f"{self._URL_BASE}/{user_id}",headers=self._HEADER_REQUEST)
        return response

    def create_user(self,payload):
        response = requests.post(self._URL_BASE,headers=self._HEADER_REQUEST,json=payload)
        return response

    def delete_user(self,user_id):
        response = requests.delete(f"{self._URL_BASE}/{user_id}",headers=self._HEADER_REQUEST)
        return response
