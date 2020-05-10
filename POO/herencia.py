"""
Inicialmente se inicia creando la clase principal Animal, la cual cuenta con tres metodos los cuales son:
    + setEspecie: Este metodo cuenta con un atributo string que nos definira de que especie es el animal
    + getEspecie: Este metodo nos retornada un string que nos dira de que especie es el animal
    + printMensaje: Este metodo imprimira en pantalla un mensaje de la clase padre
"""
class Animal:
    def setEspecie(self, species):  #Metodo para definir los valores de los atributos de la clase
        self.especies = species #Asignación de valor a atributo especies
    def getEspecie(self): #Metodo que retorna un string con la especie del animal
        return f'Soy un animal de la especie: {self.especies}' #Retorna un string
    def printMensaje(self):#Metodo para imprimir por pantalla un msj propio de la clase padre
        print('Existe una gran variedad de especies de animales') #Imprime mensaje
"""
Luego se crea la subclase Perro de la clase principal Animal, la cual cuenta con tres metodos los cuales son:
    + setRaza: Este metodo cuenta con los atributos heredados de la clase padre y adicionalmente, cuente con un
               atributo propio de tipo string que nos definira de que raza es el perro
    + getEspecie: Este metodo nos retornada un string que nos dira de que raza es el perro
    + printMensaje: Este metodo imprimira en pantalla un mensaje de la sub clase Perro
"""
class Perro(Animal):
    def setRaza(self, species, race): #Metodo para definir los valores de los atributos de la clase
        Animal.setEspecie(self, species) #Asignación de valor a atributo especies
        self.raza = race #Asignación de valor a atributo raza
    def getRaza(self):#Metodo que retorna un string con la raza del animal
        return f'Soy un Perro y soy de raza {self.raza}'#Retorna un string
    def printMensaje(self):#Metodo para imprimir por pantalla un msj propio de la subclase Perro
        print('Entre las variedades de especies de animales estan los caninos')#Imprime mensaje
"""
Luego se crea la subclase Pez de la clase principal Animal, la cual cuenta con tres metodos los cuales son:
    + setAlimentacion: Este metodo cuenta con los atributos heredados de la clase padre y adicionalmente, 
               cuente con un atributo propio de tipo string que nos definira que esta comiendo el pez
    + getAlimentacion: Este metodo nos retornada un string que nos dira que esta comiendo el pez
    + printMensaje: Este metodo imprimira en pantalla un mensaje de la sub clase Pez
"""
class Pez(Animal):
    def setAlimentacion(self, species, food):#Metodo para definir los valores de los atributos de la clase
        Animal.setEspecie(self, species)#Asignación de valor a atributo especies
        self.comida = food #Asignación de valor a atributo comida
    def getAlimentacion(self):#Metodo que retorna un string con la comida del pez
        return f'Soy un pez y estoy comiendo {self.comida}'#Retorna un string
    def printMensaje(self):#Metodo para imprimir por pantalla un msj propio de la subclase Perro
        print('Entre las variedades de especies de animales estan los peces')#Imprime mensaje
"""
Luego se crea la subclase Serpiente de la clase principal Animal, la cual cuenta con tres metodos los cuales son:
    + setVenenosa: Este metodo cuenta con los atributos heredados de la clase padre y adicionalmente, 
               cuente con un atributo propio de tipo booleano que nos definira si la serpiente es o no venenosa
    + isVenenosa: Este metodo nos retornada un booleano que nos dira que nos dira si es o no venenosa la serpiente
    + printMensaje: Este metodo imprimira en pantalla un mensaje de la sub clase Serpiente
"""
class Serpiente(Animal):
    def setVenenosa(self, species, poison=False):#Metodo para definir los valores de los atributos de la clase
        #se define un valor por defecto de veneno como False
        Animal.setEspecie(self, species)#Asignación de valor a atributo especies
        if poison == "True":#Si poison recibe True, significa que la serpiente es venenosa
            poison = True#Asignación de valor a poison
        self.veneno = poison #Asignacion de valor a atributo veneno        
    def isVenenosa(self):#Metodo que retorna booleano True si la serpiente es venenosa o False si no lo es
        if self.veneno: #Si el valor del atributo veneno es True, eso retorna.
            return True #Retorna True
        else: #Si el valor del atributo veneno es False, eso retorna.
            return False #Retorna False
    def printMensaje(self):#Metodo para imprimir por pantalla un msj propio de la subclase Perro
        print('Entre las variedades de especies de animales estan las serpientes')#Imprime mensaje
