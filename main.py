import requests #<-Importamos la librería que nos va a permitir hacer llamadas HTTP

# Importamos TODO de una librería
import random #<- Seleccionar cosas aleatorias

# from: De que librería va a sacar el módulo (PIL == pillow)
# import: Qué modulo vamos a importar específicamente
from PIL import Image, ImageFont, ImageDraw # Esta librería nos va a permitir manipular imágenes

from io import BytesIO # Ayudar a decodificar información importante



# Esta variable va a contener la respuesta de la plataforma de memes (API)
resultado = requests.get('https://api.imgflip.com/get_memes')

#Contendrá la lista de memes :D
lista_memes = resultado.json()['data']['memes'] #-> JSON == Diccionario


#len() -> El tamaño de una lista

# len() -> Me devuelve el tamaño de mi lista
tamaño_lista_memes = len(lista_memes) # La cantidad de memes que hay en mi lista

numero_aleatorio = random.randint(0, tamaño_lista_memes)

# Este print nos arroja la información de un meme aleatorio
print(lista_memes[numero_aleatorio]['url'])

# Se crea una variable para almacenar la url de nuestro meme
url_imagen = lista_memes[numero_aleatorio]['url']

# Vamos a descargar esa imagen de internet
# Primero tenemos que solicitar la información de esa imagen
imagen_info = requests.get(url_imagen)



# Aquí imprimos toda la información que se obtiene de mi imagen
# print(imagen_info.text)

# Obtenemos la información en un formato que pillow pueda abrirla
imagen_obtenida = BytesIO(imagen_info.content)

# Reescribimos la variable pero ahora ya con la imagen convertida
imagen_obtenida = Image.open(imagen_obtenida)


# Estas variables van a contener el tamaño de la imagen
largo_imagen, alto_imagen = imagen_obtenida.size

# Este valor se vaya actualizando
tamanio_fuente = 1

texto_imagen = 'Ola k ase'

# Cargarla directamente con lo que nos ofrece pillow
#fuente = ImageFont.load("arial.pil", tamanio_fuente) <- Carga fuentes en formato bitman

# Cargar la fuente de un archivo externo
fuente = ImageFont.truetype("arial.ttf", tamanio_fuente) # <- Carga en formato ttf

# Creamos un lienzo sobre nuestra imagen
lienzo = ImageDraw.Draw(imagen_obtenida)

# List Slicing <- Obtener rangos de valores de una lista

# Vamos a dibujar un recuadro donde se puede insertar texto
largo_texto, alto_texto = lienzo.textbbox((0,0), texto_imagen, font=fuente)[2:]

# Dibujamos un texto sobre la imagen
# 1. Posición en la que se va a mostrar el texto px
# 2. El texto que queremos colocar
# 3. font = Fuente que queremos utilizar
# 4. Relleno de la fuente
# lienzo.text((0,0), texto_imagen, font=fuente, fill="Black")

# Por cada iteracion que haga el ciclo le va a aumentar en 1 al tamaño de mi fuente hasta que el
# recuadro supere el tamaño de la imagen
while largo_texto < largo_imagen and alto_texto < alto_imagen:
    tamanio_fuente += 1
    # Para que se guarden los tcambios se tiene que volver a crear la variable
    fuente = ImageFont.truetype("arial.ttf", tamanio_fuente)

    largo_texto, alto_texto = lienzo.textbbox((0, 0), texto_imagen, font=fuente)[2:]

posicion_text = ((largo_imagen - largo_texto) // 2, (alto_imagen - alto_texto))

lienzo.text(posicion_text , texto_imagen, font=fuente, fill="Black")

# Mostramos la imagen al usuario
imagen_obtenida.show()
