""" EJERCICIO UNO
Una estacion de servicio dispone de 10 surtidores y necesita gestionar informacion relacionada con la venta
de combustibles en la jornada. 
De cada surtidor se conoce:
    -nro de surtidor (validar que sea ente 1 y 30)
    -cantidad: cantida dde litros de combustible vendido por surtidor (validar q sea positivo)
    - Tipo: representa el tipo de combustible. 1 = nafta 2 = nafta esepcial 3 = gasoil (validar q se ignresen valores validos)
Se pide calcular e imprimir:
    - El total de litros vendidos por tipo de combustible 
    - El nro de surtidor que menos vendio
    - El promedio por surtidor en litros de combustible vendido en la jornada (promedio general) """

totalNafta = totalEspecial = totalGas = 0
menor = None
surtidor_menor = None
total = 0

for i in range(3):
    nro = int(input("Ingrese numero de surtidor: "))
    while nro < 1 or nro > 30:
        nro = int(input("Error. Ingrese un número de surtidor válido (1-30): "))
        
    cantidad = int(input("Ingrese cantidad vendida: "))
    while cantidad < 0:
        cantidad = int(input("Error. Ingrese cantidad vendida: "))

    tipo = int(input("Ingrese tipo de surtidor. 1=nafta 2=nafta especial 3=gasoil : "))
    while tipo not in [1, 2, 3]:
        tipo = int(input("Error. Ingrese tipo de surtidor correcto: "))
        
    if tipo == 1:
        tipo_surtidor = "Nafta"
        totalNafta += cantidad
    elif tipo == 2:
        tipo_surtidor = "Nafta especial"
        totalEspecial += cantidad
    else:
        tipo_surtidor = "Gasoil"
        totalGas += cantidad
    
    if not menor or cantidad < menor:
        menor = cantidad
        surtidor_menor = nro
    
    total = totalNafta + totalEspecial + totalGas
    promedio = total / 3
    
print(f"Total vendida nafta: {totalNafta}\nTotal vendida nafta especial: {totalEspecial}\nTotal vendida gas: {totalGas}")
print("El surtidor que menos vendio fue: " + str(surtidor_menor))
print("El promedio de venta fue: " + str(promedio))






