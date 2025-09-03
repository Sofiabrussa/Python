""" ----------------------------------------LISTAS----------------------------------------------------------
Almacena una coleccion ordenada y mutable de elementos. Se definen con [] y los elementos separados por , 
Se puede agregar, quitar, o cambiar elementos de la lista """

lista1 = [1, 2, "a"]
lista2 = [0] * 20

# Append agrega elementos a una lista
# Remove quita elementos de una lista
# Len obtiene la longitud de una lista
# Reverse revierte una lista
# Sort ordena una lista

""" GENERACION POR COMPRENSION 
Permite crear listas de manera concisa basandose en una espresion 
nueva_lista =  [expresion for elemento in secuencia ] donde expresion representa el calculo que se realizara en cada elemento de la lista, 
elemento es la variable de iteracion q toma el valor de cada elemento y secuencia es la fuente de valores sobre la cual se iterara """
numeros = [1, 2, 3, 4, 5]
cuadrados = [numeros**2 for i in numeros]




