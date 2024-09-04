#Importar todo
import requests # Libreria para hacer llamadas HTTP
import random

# importa solo algo
from PIL import Image
from io import BytesIO

# Variable con respuesta de la plataforma de memes
result = requests.get(url= "https://api.imgflip.com/get_memes")

lista_memes = result.json()



