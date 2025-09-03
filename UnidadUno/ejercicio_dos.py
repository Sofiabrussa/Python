""" Ingresar un conjunto de temperatura en una lista, finalizar la carga cuando se reciba un 50
Solo aceptar temperaturas entre -20 y 49 grados
Calcular
- Cantidad de dias con temperatura bajo cero
- Promedio de temperaturas
- Promedio de temperaturas de dias calidos (+20)
- Mostrar si o no para indicar si hubo algun dia con mas de 40 grados
- Mayor temperatura de dias no calidos
- Cantidad de dias con temperatura menor al promedio
 """
 
temperaturas = []
bajo_cero = total_temp = total_calidas = cant_menor_prom = 0
calido = False

temperatura = int(input("Ingrese temperatura: "))

while temperatura != 50:
    while temperatura < -20 or temperatura > 49:
        temperatura = int(input("Error. Ingrese temperatura correcta: "))
    
    temperaturas.append(temperatura)
    total_temp += temperatura
    
    if temperatura >= 20:
        total_calidas += 1
    
    if temperatura < 0:
        bajo_cero += 1
        
    if temperatura > 40:
        calido = True
    
    temperatura = int(input("Ingrese temperatura: "))


    
temperaturas_calidas = [t for t in temperaturas if t >= 20]
temperaturas_no_calidas = [t for t in temperaturas if t < 20]
promedio = total_temp / len(temperaturas)
promedio_calidas = sum(temperaturas_calidas) / len(temperaturas_calidas) if temperaturas_calidas else 0

if calido:
    print("SI")
mayor = max(temperaturas_no_calidas)

cant_menor_prom = sum(1 for t in temperaturas if t < promedio)

print(f"las temperaturas ingresadas fueron: {temperaturas}")
print(f"La cantidad de temperaturas bajo cero fueron: {bajo_cero}")
print(f"El promedio de temperaturas es de: {promedio}")
print(f"El promedio de temperaturas calidas es de: {promedio_calidas}")
print(f"La temperatura mas alta de dias no calidos fue: {mayor}")
print(f"La cantidad de temperaturas menor al promedio es de: {cant_menor_prom}")


