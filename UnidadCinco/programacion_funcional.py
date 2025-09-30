""" ------------------------------------------- PROGRAMACION FUNCIONAL -------------------------------------------
Posibilidad de trabajar con un nuevo tipo de datos denominado "Funcion" 
- Programación estructurada --> variables almacenan valores, un único valor 
- Programación orientada a objetos --> variables pueden contener objetos, los cuales pueden tener múltiples atributos y métodos
- Programación funcional --> variables almacenan código fuente, es decir, conjuntos de instrucciones del lenguaje """


"""Variables de tipo función: Una variable puede almacenar una referencia a una función """
imprimir = print  

imprimir("Hola, mundo!")  


""" Funciones lambda: Son funciones pequeñas y concisas que se definen sin un nombre y se utilizan en el momento en que se necesitan. 
A diferencia de las funciones normales, que se definen utilizando la palabra clave def, las funciones lambda se crean utilizando la palabra clave lambda.
Una función lambda está limitada a una sola expresión y no puede contener múltiples líneas de código.
----- lambda argumentos: expresión -----
"""
suma = lambda a, b: a + b

""" ----------------------------------- Operaciones funcionales -----------------------------------"""

#- Filter: Recorre una secuencia y ejecuta por cada uno de los datos de la misma una función recibida como parámetro > filter(funcion, secuencia)
es_par = lambda x: x % 2 == 0
numeros = [2,1,35,8,5,21,4,6,9,6,3,2]
pares = list(filter(es_par, numeros))

print(pares)

#Map: Permite generar una nueva secuencia de forma tal que cada elemento se obtenga con el resultado de ejecutar una función a cada elemento de la secuencia original. > 
numeros = [2,1,35,8,5,21,4,6,9,6,3,2]
cuadrados = list(map(lambda x: x**2, numeros)) 

#Reduce: recorre una secuencia aplicando una función de reducción, obteniendo como resultado un único valor.






