""" Desarrollar un programa que lea todo el contenido del archivo numeros.txt que contiene múltiples líneas de texto, cada una de ellas con un número entero.
Al leer el archivo se debe almacenar todos los números en una lista.
A continuación el programa debe manipular los números cargados en la lista para:
- Calcular e imprimir el promedio de todos los números.
- Calcular e imprimir la cantidad de números mayores al promedio.
- Generar y mostrar una nueva lista que contenga todos los números pares. """


def leer_archivo(nombre_archivo):
    numeros = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            numeros.append(int(linea.strip()))
    return numeros


def calcular_promedio(lista):
    return sum(lista) / len(lista)

def contar_mayores_al_promedio(lista, promedio):
    contador = 0
    for numero in lista:
        if numero > promedio:
            contador += 1
    return contador


def obtener_pares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares


# Programa principal
def main():
    numeros = leer_archivo("numeros.txt")
    print("Números leídos:", numeros)

    promedio = calcular_promedio(numeros)
    print("Promedio de los números:", promedio)

    cantidad_mayores = contar_mayores_al_promedio(numeros, promedio)
    print("Cantidad de números mayores al promedio:", cantidad_mayores)

    pares = obtener_pares(numeros)
    print("Números pares:", pares)


# Ejecutar
main()

