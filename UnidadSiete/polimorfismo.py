#------------------------------------------------ POLIMORFISMO ------------------------------------------------
""" Esta característica facilita que un mismo método pueda comportarse de manera diferente según el tipo específico
del objeto que lo recibe. 
En el contexto de la herencia, el polimorfismo se manifiesta cuando las clases derivadas redefinen métodos heredados 
de la clase base, proporcionando implementaciones específicas que se ajusten a sus particulares necesidades y características."""

class Vehiculo:
    def acelerar(self):
        print("El vehículo está acelerando")

    def describir(self):
        print("Este es un vehículo genérico")

class Automovil(Vehiculo):
    #Escribo mismo metodo implementado distinto 
    def acelerar(self):
        print("El automóvil acelera suavemente")

    def describir(self):
        print("Este es un automóvil con cuatro ruedas")

class Motocicleta(Vehiculo):
    def acelerar(self):
        print("La motocicleta acelera rápidamente")

#------------------------------------------------ CLASE ABSTRACTA ------------------------------------------------
""" Una clase abstracta es aquella que no puede ser instanciada directamente y que generalmente contiene uno o más métodos abstractos.
Los métodos abstractos son declaraciones de métodos que deben ser implementados obligatoriamente por las clases derivadas, 
pero que no poseen implementación en la clase base.

Las clases abstractas sirven como plantillas que definen qué métodos deben implementar las clases derivadas """

from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

    def describir(self):
        return f"Figura: {self.nombre}!"


class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        super().__init__("Rectángulo")
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)


class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * 3.14159 * self.radio


#------------------------------------------------ INTERFAZ ------------------------------------------------
""" Las interfaces definen un conjunto de métodos que una clase debe implementar, sin proporcionar la implementación
de dichos métodos.
se pueden implementar utilizando clases abstractas que contengan únicamente métodos abstractos. 
Python permite que una clase implemente múltiples interfaces mediante herencia múltiple
"""

from abc import ABC, abstractmethod

class IVehiculoTerrestre(ABC):
    @abstractmethod
    def conducir(self):
        pass


class IVehiculoAcuatico(ABC):
    @abstractmethod
    def navegar(self):
        pass


class VehiculoAnfibio(IVehiculoTerrestre, IVehiculoAcuatico):
    def __init__(self, modelo):
        self.modelo = modelo

    def conducir(self):
        print(f"{self.modelo} está conduciendo en tierra")

    def navegar(self):
        print(f"{self.modelo} está navegando en agua")

