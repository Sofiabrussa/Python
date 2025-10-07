class Base:
    def saludar(self):
        print("Hola desde la clase BASE")

class Padre(Base):
    def saludar(self):
        print("Hola desde la clase PADRE")

class Hermana(Padre):
    def saludar(self):
        print("Hola desde la clase HERMANA")

class Hija(Padre):
    pass  # No redefine el método saludar

# Creamos una instancia de Hija
objeto = Hija()
objeto.saludar()
