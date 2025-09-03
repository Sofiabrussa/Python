"""------------------------------------------DICCIONARIOS------------------------------------------
Estructura de datos que almacena pares de datos conocidos como "clave" y "valor". La clave actua 
como identificador unico para un dato especifico. 
Alta velocidad de busqueda
No permiten claves duplicadas y no hay un indice de posicion 
"""

"""------------------------------------------CREACION DICCIONARIOS------------------------------------------
dict() = inicializa un diccionario vacio 
{} = se enumeran los valores separados por coma y la separacion de calve valor con :
comprension
"""

"""------------------------------------------ACCESO DICCIONARIOS------------------------------------------
Utilizando [] y con la clave del valor que se quiere obtener. 
get() = Recibe comp parametro la clave que se busca 
"""

"""------------------------------------------RECORRIDO DICCIONARIOS------------------------------------------
keys() = Retorna un conjunto con todas las claves
values() = retorna una lista con todos los valores
items() = retorna una secuencia de tuplas
"""

diccionario = {1: "Lunes", 2: "Martes", 3: "Miercoles"}

for nro, nombre in diccionario.items():
    print(f"EL dia {nro} se llama {nombre}")