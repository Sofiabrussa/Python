
"""------------------------------------------CONJUNTOS------------------------------------------
Estructura de datos que permite almacenar y manipular colecciones de elementos. 
Elimina automaticamente elementos duplicados
No admiten acceso indexado
Busuqeda mas rapida porque no recorre cada elemento sino que los localiza en base a su criterio 
de dispersion 
"""


"""------------------------------------------CREACION DE CONJUNTOS------------------------------------------
set() = Crea un conjunto vacio 
{} = Crea un conjunto con elementos separados por ,
comprension de conjuntos 
"""

"""------------------------------------------INSERCION DE CONJUNTOS------------------------------------------
add() = Agrea un nuevo elemento 
update() = Recibe como parametro una secuencia iterable, como un rango, una cdena, etc. Recorre todos los 
elementos de la secuencia iterable y los inserta en el conjutno original.
"""

"""------------------------------------------ELIMINCACION DE CONJUNTOS------------------------------------------
remove() = recibe como parametro el valor que se desea eliminar. Si el elemento no existe, lanza un error
discard() = Elimina el elemento indicado. Si el elemento no existe, no pasa nada (no da error).
pop() = Elimina y devuelve un elemento cualquiera del conjunto (porque los conjuntos no tienen orden).
Si el conjunto está vacío → da error (KeyError)
clear() = Elimina todos los elementos del conjunto, dejándolo vacío.
"""

"""------------------------------------------RECORRIDOS DE CONJUNTOS------------------------------------------
Se utiliza for. Siempre recorre de forma distinta porque los conjuntos no estan ordenados segun la insercion sino
que por dispersion.
Para recorrer un conjutno ordenado se utiliza el metoso sorted() pero rodenados segun sus valores.
"""

"""------------------------------------------OPERACIONES DE CONJUNTOS------------------------------------------
Pertenencia = operador "in" para saber si el elemento se encuentra en el conjunto
Union = une conjutos mediante "union" sin tener en cuenta los repetidos
Interseccion = Devuelve un conjunto con los valores en comun de dos colecciones con el metodo "intersection()"
Diferencias = Devuelve un conjunto con los elementos presentes en el primer conjunto pero no en el segundo con el metodo difference_update()
Para traer las deferencias entre dos conjuntos se usa symmetric_difference()
"""


""" En este ejemplo se dispone de una lista llamada lista que contiene elementos duplicados.
Para eliminar los duplicados, se convierte la lista en un conjunto utilizando la función set().
Los conjuntos en Python sólo pueden contener elementos únicos, por lo que al convertir la lista en un conjunto, automáticamente se eliminan los elementos duplicados.

Luego se convierte nuevamente el conjunto a una lista utilizando la función list() y se asigna en una nueva lista llamada lista_sin_duplicados que contiene los
elementos de la lista original sin duplicados.

Finalmente, se imprime la lista sin duplicados para verificar el resultado. """
# Lista con elementos duplicados
lista = [1, 2, 3, 4, 2, 3, 5, 6, 1, 7, 8, 5, 9]

# Convertir la lista en un conjunto para eliminar duplicados
conjunto = set(lista)

# Convertir el conjunto nuevamente a una lista
lista_sin_duplicados = list(conjunto)

# Imprimir la lista sin duplicados
print(lista_sin_duplicados)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

