""" ----------------------------------------CADENAS----------------------------------------------------------
Secuencia mas simple y se delimita con comillas. El operador suma + une dos cadenas y el operador de multiplicacion * las repite  """

mensaje1 = "Hola"
mensaje2 = "Mundo"

mensaje_concatenado = mensaje1 + " " + mensaje2
subcadena = mensaje1[1:3]

#Find busca una subcadena e informa la posicion 
#Replace reemplaza todas las apariciones de una subcadena por otra 
#Strip Elimina todos los espacios que se encuentran al inicial y al final 
#Split divide la cadena cin un delimitadot y devuelve una lista con los valores extraidos

""" CADENAS FORMATEADAS
Permiten agregar dentro de la cadena dentro de {} el valor de una variable. Se debe indicar al principio la letra f  """
saludo = f"{mensaje1} {mensaje2}! como estas? "

print(mensaje_concatenado, subcadena, saludo)

""" ----------------------------------------TUPLAS----------------------------------------------------------
Almacena una secuencia ordenada e inmutable de elementos. Se definen con () o separando elemtnos con , 
Inmutables porque no se pueden cambiar posterior a su creacion."""

tupla1 = (1, 2, 3)
tupla2 = "a", "b", "c"

