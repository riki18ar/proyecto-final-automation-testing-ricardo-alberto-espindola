import requests
import pytest
import pytest_check as check
from faker import Faker
from datetime import datetime
from conftest import logger
fake = Faker()

# Función para validar la respuesta de una petición HTTP.
def validate_date_response(response, excpected_status,expected_fields=None,max_time=1.0):
    # Nivel 1: Código de estado
    assert response.status_code == excpected_status
    # Nivel 2: Headers
    # Especial manejo para respuestas sin contenido (204 No Content)
    if excpected_status != 204: 
        assert "application/json" in response.headers.get("Content-Type", "")
    # Nivel 3-4 : Estructura y tipos de datos
    # Validar que los campos esperados están presentes en la respuesta JSON
    if expected_fields and response.text:
        body = response.json()
        assert expected_fields <= set(body.keys())
    # Nivel 5: Tiempo de respuesta
    assert response.elapsed.total_seconds() < max_time
    assert response.json() if response.text else {}    

# Clase de pruebas para obtener usuarios.
class TestGetUsers:
    URL_API = "https://jsonplaceholder.typicode.com/"
    # Marca para identificar la prueba como de tipo GET
    @pytest.mark.get
    # Prueba para verificar el código de respuesta de la petición GET /users
    def test_get_response_code(self, api_url):
        response = requests.get(api_url + "/users")
        data = validate_date_response(
            response= response,
            excpected_status=200, 
            expected_fields=[], 
            max_time=2.0
        ) 
    # Prueba para verificar los datos de la respuesta de la petición GET /users
    @pytest.mark.get 
    def test_get_response_data(self, api_url):
        response = requests.get(api_url + "/users")
        data = response.json()
        # Verifica que la lista de usuarios no está vacía. 
        assert len(data) > 0
        assert isinstance(data, list)
    # Verifica que la estructura de los datos del primer usuario es correcta.
        first_user = data[0]
        print(first_user)
    # Comprobar la estructura de llaves del usuario    
        key_structure = {"id", "name", "username", "phone", "address", "website"}
    # Verifica que todas las llaves esperadas están presentes en el primer usuario
        for i in key_structure:
            # Informa si falta alguna llave en el primer usuario.
            assert i in first_user , f"la llave {i} no esta en el {first_user}"
class TestPostUser:
    URL_API = "https://jsonplaceholder.typicode.com/"

    @pytest.mark.post
    def test_post_response_code(self, api_url):
        new_user = {
            "name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "createdAt": "2024-06-10T12:00:00Z"
            }
        
        response = requests.post(api_url + "/users", new_user)
        assert response.status_code == 201 

        data = response.json()
        print(data)
        assert "id" in data       

        if "createdAt" in data:
            created_at = data["createdAt"]
            current_year = datetime.now().year
            assert str(current_year) in created_at , f"no esta en el año actual"
class TestDeleteUser:
    URL_API = "https://jsonplaceholder.typicode.com/"
    @pytest.mark.delete
    def test_delete_response_code(self, api_url):
        response = requests.delete(api_url + "/users/1")
        assert response.status_code == 200

class TestUserWorksFlow:
    
    def test_completo_users(self,api_url):
        logger.info("TEST ENCADENADO DE USUARIOS: GET, POST, PUT, PATCH, DELETE")
        logger.info("1.GET Obtener usuarios")
        # GET OBTENER USUARIOS
        response = requests.get(api_url + "/users")
        data = response.json()
        check.equal(response.status_code, 200)
        check.is_true(len(data) > 0)
        print("1.POST Crear un nuevo usuario")

        new_user = {
            "name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            }
        
        response = requests.post(api_url + "/users", new_user)
        assert response.status_code == 201 