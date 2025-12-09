import csv
import json
from pathlib import Path

# Función para obtener casos de prueba de login desde un archivo CSV.
def get_login_csv(csv_file="data_login.csv"):
    # Construye la ruta absoluta al archivo CSV en la carpeta "data".    
    csv_file = Path(__file__).parent.parent / "data" / csv_file
    # Lista para almacenar los casos de prueba.
    casos = []
    # Abre el archivo CSV y lee su contenido.
    with open(csv_file, newline="") as h:
        read = csv.DictReader(h)
        # Itera sobre cada fila del archivo CSV.
        for i in read:
            username = i["username"]
            password = i["password"]
            login_example = i["login_example"].lower() == "true"
            casos.append((username, password, login_example))
    # Devuelve la lista de casos de prueba.
    return casos
