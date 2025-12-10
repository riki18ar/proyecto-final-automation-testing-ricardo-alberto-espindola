import requests

# Definición de la URL base de la API.
URL_API = "https://jsonplaceholder.typicode.com/"

# Función para obtener usuarios desde la API.
def get_users():
    print("Obteniendo usuarios desde la API...")
    response = requests.get(URL_API + "users")
    print(response.status_code)
    assert response.status_code == 200
    data = response.json()
    print(data)
# Función para crear un nuevo usuario en la API.
def post_user():
    print("Creando un nuevo usuario en la API...")
    new_user = {
        "name": "Juan Perez",
        "email": "juanperez@gmail.com",
        "phone": "123-456-7890"
        }
    response = requests.post(URL_API + "users", new_user)
    print(response.status_code)
    assert response.status_code == 201

    data = response.json()
    print(data)
# Función para actualizar un usuario existente en la API.
def put_user():
    print("Actualizando un usuario en la API...")
    user_update = {"id": 1,
        "name": "hola mundo",
    }
    response = requests.put(URL_API + "users/1", user_update )
    print(response.status_code)
# Función para actualizar parcialmente un usuario en la API.
def patch_user():
    print("Actualizando un usuario en la API con PATCH...")
    user_update = {"id": 1,
        "email": "hola@gmail.com",
    }
    response = requests.patch(URL_API + "users/1", user_update )
    print(response.status_code)
# Función para eliminar un usuario en la API.
def delete_user():
    print("Borrando usuario en la API...")
    response = requests.delete(URL_API + "users/1")
    print(response.status_code)
#get_users()
#post_user()
#put_user()
#patch_user()
delete_user()