# Clase base
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

# Clase derivada
class Estudiante(Persona):
    def __init__(self, nombre, carrera):
        # Llamamos al constructor de la clase base
        super().__init__(nombre)
        # Agregamos un nuevo atributo propio de la clase derivada
        self.carrera = carrera

# Ejemplo de uso
alumno = Estudiante("Camila", "Gestión Ambiental")
print(alumno.nombre)    # Heredado de Persona
print(alumno.carrera)   # Propio de 


