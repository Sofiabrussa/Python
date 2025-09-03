#FUNCIONES
# Se definen usando la palabra "def" seguida del nombre de la funcion y parentesis para los parametros
# Si no coloco return, la funcion devuelve none

def calcular_area (base, altura):
    area = (base * altura) / 2
    return area

area = calcular_area(3, 5)

#-------------------------------------------------------------------------------
# PARAMETROS

# PARAMETROS POSICIONALES
# Se pasan a la funcion en el mismo orden en el que se definen.Son obligaotrios
def saludar(nombre, edad):
    mensaje = "Hola", nombre
    return mensaje

mensaje = saludar("jose", 24)

# PARAMETROS CON VALOR PREDETERMINADO
# Tienen un valor asignado por defecto en caso que no se les pase un valor. 

def saludar1(nombre, edad=30):
    mensaje = "Hola", nombre
    return mensaje

mensaje = saludar1("jose")

#PARAMETROS DE PALABRA CLAVE
# Se especifican durante la llamada a la funcion con el formato nombre_parametro = valor. Permiten mandar parametros en cualquier orden
def saludar2(nombre, edad):
    mensaje = "Hola", nombre
    return mensaje

mensaje = saludar2(edad=24, nombre="jose")

#PARAMETROS VARIABLES *ARGS
# Permite pasar un nro variable de argumentos posicionales. Se agrupan en una tupla dentro de la funcion 

def sumar(*nros):
    total = 0 
    for num in nros:
        total += num
    return total

rta = sumar(1,2,3,4,5)

#PARAMETROS DE PALABRAS CLAVE VARIABLES **KWARGS
#Permite pasar un nro variable de argumentos de palabra clave a una funcion. Se agrupan en un diccionario

def imprimir_datos(**datos):
    for clave, valor in datos.items():
        print(clave + ":", valor)

# datos.items() obtiene una lista de tuplas
# [("nombre", "Sofía"), ("edad", 25), ("ciudad", "Rosario")]
imprimir_datos(nombre= "juan", edad=25, ciudad="pinamar")


#-------------------------------------------------------------------------------
# RETORNOS
# Las funciones puedenr etornar cero, uno o mas expresiones como rta. En el caso de no inlcuir alguna, entrega None
# Para que una funcion retorne mas de un valor, se los debe indicar separados por coma
