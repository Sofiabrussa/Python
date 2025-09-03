#ESTRUCTURAS CONDICIONALES

# IF
# Permite ejecutar un bloque de acciones si se cumple una condicion.
#Se puede combinar con else o elif para definidir otros casos alternativos. Else se usa para ejecutar un bloque de codigo si la condicion no se cumple 
# y elif se usa para evaluar otra condicion despues del if.
x = 10
if x > 0:
    nro = "Positivo"
elif x < 0:
    nro = "Negativo"
else:
    nro = "Es cero"
    
#-------------------------------------------------------------------------------
#Una condición puede ser:
# - Una constante booleana → True o False.
# - Una variable que guarde un valor booleano.
# - El resultado de una operación → como x > 10. """

# BANDERAS
# A veces tenemos variables que ya son True o False. En esos casos no hace falta compararlas con True o False
existe = True

if existe:
    print("Existe")

if not existe:
    print("No existe")

#-------------------------------------------------------------------------------
# Truthiness
# Todo valor de tipo diferente a bolean puede ser interpretado como si fuera verdadero o falso 
# En general se considera falso todo dato "vacio"

nombre = "Sofi"
edad = 24

if not nombre: print("NO ingreso nombre")
if not edad: print("NO ingreso edad")

print("Su edad es" + ("impar" if edad % 2 else "par"))