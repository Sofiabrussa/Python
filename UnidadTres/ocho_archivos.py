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
"""
