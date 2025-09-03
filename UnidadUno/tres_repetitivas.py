#ESTRUCTURAS REPETITIVAS

# FOR
# Permite iterar sobre una secuencia de elementos
# La variable elemento toma el valor de cada elemento de la secuencia en cada iteracion. El bloque se ejecuta en cada iteracion.
# El bucle termina cuando se recorre toda la secuencia o con una instruccion "break"

frutas = ["manzanda", "banana", "frutilla"]

for fruta in frutas:
    print(fruta)
    
#-------------------------------------------------------------------------------
# WHILE
# Crear un bucle que se repite mientras se cumple una condicion. 
# La condicion es una expresion que se evalua en cada iteracion hasta que de falsa y termina el bucle

nro = 572
suma = 0

while nro > 0:
    digito = nro % 10 #te da el último dígito
    
    suma += digito #Suma ese dígito a la suma total.
    
    nro //= digito #elimina el último dígito.
print ("La suma de digitos es:" + suma)

#-------------------------------------------------------------------------------
# SALTOS
# Break se utiliza para terminar un bucle antes de que se complete su condicion de finalizacion. 
# Continue se utiliza dentro de ciclos para omitir el resto del codigo en una iteracion actual y pasar a la siguiente

# CLAUSULA ELSE
# Se utiliza para especificar un bloque que se ejecuta cuando el ciclo termino de iterar todos lso elementos o cuando la condicion es falsa
texto = input ("Ingrese un texto:")

for letra in texto:
    if letra == "a":
        print("Contiene la letra a")
        break
else:
    print("No contiene la letra a")


