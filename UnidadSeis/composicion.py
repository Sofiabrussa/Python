class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = []  # relación: acá se guardan los Jugadores

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

# Uso de composicion
e = Equipo("River")
e.agregar_jugador(Jugador("Martínez"))
e.agregar_jugador(Jugador("Gómez"))

print(f"Equipo {e.nombre} tiene {[j.nombre for j in e.jugadores]}")
