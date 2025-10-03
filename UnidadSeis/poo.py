#------------------------------------------ CLASES ------------------------------------------ 

class Persona:
    """ Gracias al __init__, no hay que asignar los valores manualmente después, el objeto nace ya con sus atributos cargados. """
    """ self es una referencia al propio objeto que se está creando o usando. Te permite decir: “este atributo pertenece a este objeto en particular”. """
    def __init__(self, documento=0, nombre="No", apellido="No", edad=0 ):
        self.documento = documento
        self.nombre= nombre
        self.apellido = apellido
        self._edad = edad

    def nombre_completo (self):
        return f"{self.nombre} {self.apellido} "
    
    # @property es un decorador que convierte un método en un atributo de solo lectura (getter).
    """_edad = el “cajón” real donde se guarda el dato.
    edad = la “puerta de acceso” controlada al cajón (que pasa por el getter y setter). """
    @property
    def edad(self):            
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):  # setter
        if nueva_edad >= 0:
            self._edad = nueva_edad  #El _ es para guardar el nuevo valor al atributo
        else:
            print("La edad no puede ser negativa")
    
    #Funcion magica para poder imprimir en formato texto un objeto
    def __str__(self):
        return f"{self.nombre} {self.apellido}, tiene {self._edad} años (DNI {self.documento})"
    
    def __add__(self, other):
        if isinstance(other, Persona): #protege tu método mágico para que solo funcione con objetos del tipo esperado
            return Persona(
                nombre=f"{self.nombre}-{other.nombre}",
                apellido=f"{self.apellido}-{other.apellido}",
                edad=self._edad + other._edad
            )
            
    
    
""" Para instanciar objetos """
a = Persona() #Los atributos se inicializan con valores por defecto
b= Persona(43370803, "Sofia", "Brussa", 43) #Atributos se inicializan con los valores dados
c= Persona(documento=4380563, edad=20) #Documento se inicializa con ese atributo y los demas por defecto

""" #Enviar mensajes entre objetos """
print(b.nombre_completo())

""" Encapsulamiento
Parece que accedés a un atributo normal (b.edad), pero por detrás se están ejecutando los métodos getter y setter que controlan la lectura y escritura. """
print(b.edad)   # usa el getter -> devuelve 4.

b.edad = 30     # usa el setter -> cambia la edad a 30
print(b.edad)  

""" Imprimir un objeto gracias a __Str__ """
print(b)
print(b+c)