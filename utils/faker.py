from faker import Faker

# Se instancia el objeto Faker para generar datos falsos.
fake = Faker() 
# Función para generar casos de prueba de login utilizando Faker.
def get_login_faker(num_casos=5):
    # Genera una lista de tuplas con datos de login falsos.
    casos = []
    # Bucle for para crear el número especificado de casos de prueba, con un nombre de usuario, contraseña (de longitud 12) y un booleano aleatorio.
    for _ in range(num_casos):
        username = fake.user_name()
        password = fake.password(length=12)
        login_example = False 
        # Añade la tupla (username, password, login_example) a la lista de casos.
        casos.append((username, password, login_example))
    return casos