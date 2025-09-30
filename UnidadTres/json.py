"""--------------------------------- ARCHIVOS JSON ---------------------------------"""
""" Es un formato de intercambio de datos que se utiliza para representar información estructurada de manera legible tanto para
humanos como para máquinas.
Los archivos JSON están compuestos por una colección de pares clave-valor """

import json

# Abre el archivo JSON en modo lectura
with open('datos.json', 'r') as archivo:
 datos = json.load(archivo)

# Ahora, 'datos' es un diccionario que contiene la información del archivo JSON
print(datos['nombre']) 
print(datos['edad']) 
print(datos['pasatiempos']) 
