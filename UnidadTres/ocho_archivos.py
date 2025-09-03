"""------------------------------------------ARCHIVOS------------------------------------------
Los archivos son el mecanismo mas basico para poder almacenar datos de forma persistente. Permiten que un
programa almacene datos en un archivo y que otro programa pueda manipular esos datos, incluso si es otro
otro lenguaje.
"""

"""------------------------------------------TIPOS DE ARCHIVOS------------------------------------------
-Archivos de texto: Contienen informacion representada como una secuencia de caracteres legibles, 
texto plano. 
-Archivos binarios: Contienen informacion no legible para humanos, utilizan representacion binaria. 
Para almacenar datos mas complejos
"""

"""------------------------------------------APERTURA Y CIERRE------------------------------------------
Para trabajar con un archivo en python, es necesari informarle al sop que archivo se pretende utilizar, donde 
esta ubicado y que operaciones se van a realizar en el. Para esto se debe realizar la operacion de apertura del 
archivo. 
El cierre de un archivo notifica al sop que ya no se esta utilizando por lo tanto otros programas pueden 
accder a el y ademas garantiza que las escrituras se guarden correctamente.

OPEN= funcion que recibe dos parametros, el nombre del archivo y/o ubicacion y el otro es el modo de apertura. 
Devuelve una estructura de datos que nos permite operar con el archivo 
"""

"""------------------------------------------MODOS DE APERTURA------------------------------------------
Es una cadena de texto que puede tener una o dos letras y son las que indican la operacion a realizar. 
W = Si el archivo no existe, se crea uno. Si el archivo existe, se borra el contenido y se empieza desde cero
X = Es utilizado para escribir en un archivo completamente nuevo sin sobrescribir uno existente
A = Si el archivo no existe, se crea. Si existe, el contenido previo no se borra, se sobreescribe
R+ = Permite tanto lectura como escritura  
"""

"""------------------------------------------LECTURA DE ARCHIVOS------------------------------------------
read = lee todo el conteido y lo devuelve en una variable string. Es para textos pequeños
readline = Lee de a una linea por llamado. Devuelve una cadena con el contenito de una linea y permite la lectura
en ciclo. Es para archivos grandes
readliness = Lee cada una de las lineas, devolviendo una lista donde cada posicion contiene una linea de texto
"""

archivo = open("./datos.txt")
contenido = archivo.read()
print(contenido)
archivo.close()

archivo = open("./datos.txt")
linea = archivo.readline()
while linea:
    print(linea)
    linea = archivo.readline()

archivo.close()


"""------------------------------------------ESCRITURA DE ARCHIVOS------------------------------------------
write = permite escribir una cadena en el archivo
writelines = recibe una lista de cadenas y escribe cada una de ellas en el archivo en el orden en que 
aparezcan en a lista.
"""

nombres = ["juan", "Maria", "Carlos"]

with open("./datos.txt", "a") as archivo:
    for nombre in nombres:
        archivo.write(nombre + "\n")

# Leer lo que se escribió
with open("./datos.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:\n", contenido)

