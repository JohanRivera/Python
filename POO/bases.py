#La POO es un modelo básico de diseño y desarrollo de programas
# Es modelar cosas de la vida real al codigo mediante clases, y adicionalmente se reutiliza
# código al modelar las cosas.

"""
DIAGRAMA DE CLASES UML
    Características de los diagramas de clases
        Estos se dividen jerarquicamente en:
            *Clases: Sirve para representar las cosas de un sistema, por ejemplo en un zoologico serían
            animales
            *Atributos: Contiene los valores que describen cada instancia de la clase, en el ejemplo del 
            zoologico serían las características iguales de los animales, ej: nombre, edad, especie, id.
            *Métodos: Operaciones o funciones, que permiten especificar cualquier comportamiento de una clase.
        Por lo tanto, el ejemplo anterior en diagram de clases UML, se vería:
        ------------------------
        |        ANIMALES      |      <---- Clase
        ------------------------
        |    -nombre: str      |
        |    -edad: int        |     <---- Atributos
        |    -especia: str     |
        |    -id: str          |
        ------------------------
        |   -definirNombre()   |
        |   -comen()           |     <---- Métodos 
        |   -tenerCrias()      |
        ------------------------
        
        Ahora, se tendrá en cuenta la visibilidad, el cual define la accesibilidad para el atributo o método.
        Esto se identifica en:
            *Privado: Ninguna clase o subclase puede acceder a estos, se identifica con el -
            *Público: Cualquier clase o subclase puede acceder a estos, se identifica con el +
            *Protegido: Solo la misma clase o subclase puede acceder a estos, se identifica con el #
            *Paquete / defecto: Puede ser usada por cualquier clase mientras este en el mismo paquete, se
            identifica con la ~

    Relaciones entre clases
        *Herencia: Se crean subclases para heredar los datos de la clase principal, se relaciona mediante 
        flechas como por ejemplo:

        ------------------------
        |        ANIMALES      |  
        ------------------------                                   ---------------------
        |    -nombre: str      |<--------------------------------- |      Nutria       |
        |    -edad: int        |            -----------------       --------------------
        |    -especia: str     |<-----------|    tortugas   |      |                   |
        |    -id: str          |            -----------------      | -bigotes: int     |
        ------------------------            |               |      |                   |
        |   -definirNombre()   |            |               |      ---------------------
        |   -comen()           |            |               |      |                   |
        |   -tenerCrias()      |            -----------------      |                   |
        ------------------------            |               |      ---------------------
                                            -----------------                  |
                                                                               |
        *Asociación: No es una dependencia, por ejemplo, las nutrias           |
        comen erizos de mar y se representa mediante una linea simple.         |
                                                                               |
                                            ---------------                   comen
                                            | erizo de mar|                    |
                                            ---------------                    |
                                            |             |---------------------
                                            |             |
                                            ---------------
                                            |             |
                                            ---------------
        
        *Agregación: Esta es una relación en un todo, pero no dependen de ellas, por ejemplo,
        un tortuguero (centro de tortugas), crea una agregación con las tortugas (se representa
        con una linea simple) y las tortugas hacen parte de este todo que es la clase tortuguero
        pero las tortugas pueden y no ser parte de este todo y aún así seguir existiendo.

        *Composición: Esta relación es una dependencia entre la clase principal y las sub clases, en donde
        si se destruye la clase principal todas las subclases no podrían existir. Se representa mediante
        un diamante.

        *Multiplicidad: Es igual a la relación anterior, pero con la diferencia que se puede limitar el 
        número de tipos de subclases que hayan de algo. Por ejemplo en una casa (clase) quiero que solo
        haya un baño (sub clase) pero cuantas alcobas (subclase) se deseen. Estas se representan mediante el
        diamante y mediante el uso de:
            - 0..1 cero a uno(opcional) 
            - 0..* cero a cuantas se desee
            - 1..* uno a cuantas se desee
            - n (cantidad especifica) 
            - m - n (rango especifico bv vFZc)
"""

# ------------------------ CLASES, OBJETOS Y MÉTODOS ------------------------------------------
# Para dejar una clase o función vacia sin que presente problema se coloca 'pass' en el interior de estas.
# Por otro lado, existen las clases y las instancias de clases, en donde las clases (esquema) son los planes 
# para crear nuestras instancias, y las instancias (llenar el esquema)serían en caso de empleado los empleados. 
class Employee: #Clase
    def __init__(self, first, last, pay): #Esto es otro ejemplo de un método 
        self.first = first #Estos son los atributos de la clase
        self.last = last #Estos son los atributos de la clase
        self.pay = pay #Estos son los atributos de la clase
        self.email = first + '.' + last + "@hotmail.com" #Estos son los atributos de la clase
    
    def fullname(self): #Esto es un ejemplo de un metodo o contructor
        return '{} {}'.format(self.first, self.last)
    
    def addPay(self, newPay): #Otro ejemplo de un metodo o constructor
        self.pay = self.pay + newPay

emp_1 = Employee('Johan','Rivera',1200000) #Instancias de la clase
emp_2 = Employee('Leandro','Garzón',1500000) #Instancias de la clase

print(emp_1.email) #Llamar un atributo sin ningún metodo
print(Employee.fullname(emp_1)) #Otra forma de utilizar un metodo
print(emp_2.fullname()) #Utilizar un método
emp_1.addPay(100000)
print(emp_1.pay)

# --------------------- FUNCIONES CON ATRIBUTOS ----------------------------------------
class Person:
    age = 27
    name = 'Johan'
    country = 'Colombia'

doctor = Person() 
print('the age is: ', doctor.age)
print('the age is: ', getattr(doctor,'age'))#Different form to recieve the value the way direct

print('the doctor has a age? ', hasattr(doctor,'age'))#This function return a value boolean

print('the name is: ', doctor.name)
setattr(doctor, 'name', 'Leandro') #This function is a change of value in the atributte
print('Now the name is: ', doctor.name)

#delattr(doctor, 'country') #This function delete the atribute

# ----------------------------- HERENCIA -----------------------------------------------------

class Pokemon: #Main class
    pass
    def __init__(self, name, element):
        self.name = name
        self.element = element
    
    def description(self):
        return 'The name of the Pokemon is {} and his element is {}'.format(self.name,self.element)
    

class Pikachu(Pokemon):#Sub class
    def atack(self,typeAtack):
        return 'The name of the Pokemon is {} and the type of atack is {}'.format(self.name, typeAtack)
    
class Charmander(Pokemon):#Sub class
    def atack(self,typeAtack):
        return 'The name of the Pokemon is {} and the type of atack is {}'.format(self.name, typeAtack)
    
newPokemon = Charmander('Dragonite','Fire')
print(newPokemon.description())
print(newPokemon.atack('Fire ball'))

#Example in class and herency
class Calculator:
    def __init__(self,num):
        self.n = num
        self.datas = [0 for i in range(num)] #This is to know how many items will be ordered

    def enterData(self):
        self.datas = [int(input('Enter data ' + str(i+1) + ' = ')) for i in range(self.n)]

class Basicoperations(Calculator):
    def __init__(self):
        Calculator.__init__(self,2)

    def add(self):
        a, b, = self.datas
        s = a + b
        print('The result is ', s)

    def substraction(self):
        a, b, = self.datas
        r = a - b
        print('The result is ', r)
    
    def multiplication(self):
        a, b, = self.datas
        x = a * b
        print('The result is ', x)
    
    def division(self):
        a, b, = self.datas
        z = a / b
        print('The result is ', z)

class Root(Calculator):
    def __init__(self):
        Calculator.__init__(self,1)
    
    def square(self):
        import math 
        a, = self.datas
        print('The result is ', math.sqrt(a))

miniCalculator = Basicoperations()
#miniCalculator.enterData()
#miniCalculator.add()

mini2Calculator = Root()
#mini2Calculator.enterData()
#mini2Calculator.square()

newObject = Basicoperations()
print(isinstance(newObject,Basicoperations)) # Verify if the new object is working with the function indicate
#this function return a boolean, in this example newObject is a object of Bascioperations

print(issubclass(Basicoperations,Calculator)) #Verify the herency of class, in this example Basicoperations
#is a subclass of Calculator

# ----------------------------------- HERENCIA MÚLTIPLE ------------------------------------------------
"""
La herencia multiple se refiere a la posibilidad de crear una clase a partir de múltiples clases superiores,
como se observa en el siguiente esquema:
    class Base_one:
        pass

    class Base_two:
        pass

    class Multiplederivative(Base_one, Base_two):
        pass

Por otro lado, también existe la herencia multinivel, en donde las características de la clase base y la clase
derivada se heredan en la nueva clase derivada, como se observa en el siguiente esquema:
    class Base_one:
        pass

    class Derivative_one(Base_one):
        pass

    class Multiplederivative(Base_one, Derivative_one):
        pass
"""
#Example

class Phone:
    def _init__(self):
        pass

    def call(self):
        print('Calling...')

    def occupied(self):
        print('Ocupied...')

class Camera:
    def __init__(self):
        pass

    def photografic(self):
        print('Taking photo...')

class Player:
    def __init__(self):
        pass

    def playMusic(self):
        print('Play music...')
    
    def playVideo(self):
        print('Play a video...')

class SmartPhone(Phone, Camera, Player):
    def __del__(self): #Is to clean up resources, is to make the process faste. Remove junk classes
        print('SmartPhone power off...')


myphone = SmartPhone()
#print(dir(myphone)) #This are the special methods that i can use in this object 
print(myphone.photografic())

# --------------------------------- F-STRING -------------------------------------------
#format %
course = 'python'
print('Learning %s' %course)
name = 'Johan'
age = 25
print('Hello I am %s and I am %s age' %(name, age)) #How to use

#str.format()
print('How are you? I am {} and my age is {}'.format(name,age))#How to use

print(f"Hi i am {name} and my age is {age}")#How to use
#Example in a class

class Student:
    def __init__(self, name, last, age):
        self.name = name
        self.last = last
        self.age = age
    #def __str__(self): #This function is used only to show us anything whitout import the attributes
     #   return f'Complete name: {self.name} {self.last}, Age: {self.age}'
    def __repr__(self): #This function respect the attributes and their properties
        return f'Complete name: {self.name} {self.last}, Age: {self.age}'

new_student = Student('Johan Leandro','Rivera Garzón', 20)
#print(f'{new_student}') Method for use the __str__
print(f'{new_student !r}') #Method more recommendable because respect the attributes

# ------------------------------------- Métodos: Clase y Estáticos ----------------------------------
"""
The different between class and instance is:
    *Class is a model for create instances 
    *Instance is a instance class
In python exists three types of methods, these are: 
    *Static methods:
        To create this method we nedd the word reserved @staticmethod, we can call this method wihtout any
        instance class. Besides, this type of method doesn't use access to the outside, thus, this method
        can't access to any other attribute or call to any other function inside of the class. For example:
"""
class Cake:
    def __init__(self, ingredients, size):
        self.ingredients = ingredients
        self.size = size

    def __repr__(self): 
        return f'Cake({self.ingredients !r}, 'f'{self.size})'

    def area(self):
        return self.size_area(self.size)

    @staticmethod
    def size_area(area2):
        import math
        return area2 ** 2 * math.pi

new_cake = Cake(['Sugar', 'Flour', 'Milk', 'Cream', 'Egg'], 5)
print(new_cake.size_area(10))

"""

    *Class methods:
        To create this method we need the word reserved @classmethod, we can call this method whitout any
        instance class. For example: 
"""
class Cake2:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self): 
        return f'Cake2({self.ingredients !r})'

    @classmethod
    def chocolate_cake(cls): #When we work with classmethod the method recieves the word reserved 'cls'
        return cls(['sugar', 'flour', 'milk', 'egg', 'chocolate'])

    @classmethod
    def vanilla_cake(cls):
        return cls(['sugar', 'flour', 'milk', 'egg', 'vanilla'])

print(Cake2.chocolate_cake())
"""
    *Instance methods: This method is the comun.
"""

#--------------------------------------- Polymorphism ---------------------------------------------------
"""
Is the capacity of the objects in differents class to use a behavior or attribute with the same name but
with different value. For example: In this example, we create a method called 'animal_type' where the class
instance create again this method with the same name but with a different value
"""
class Animals: 
    def __init__(self, name):
        self.name = name
    def animal_type(self):
        pass

class Lion(Animals):
    def animal_type(self):
        print('Wild animal')

class Dog(Animals):
    def animal_type(self):
        print('Domestic animal')

new_dog = Dog('IDK')
new_dog.animal_type()

#--------------------------------------- Polymorphism for function --------------------------------------------

class Tomato: 
    def ctype(self):
        print('Vegetable')

    def colour(self):
        print('Red')

class Apple: 
    def ctype(self):
        print('Fruit')

    def colour(self):
        print('Green')

def new_function(obj):
    obj.ctype()
    obj.colour()

new_tomato = Tomato()
new_apple = Apple()
new_function(new_tomato)
new_function(new_apple)

# ------------------------------------- Polymorphism with method -----------------------------------------------

class Colombia:
    def capital(self):
        print('Bogotá')
    
    def language(self):
        print('Spanish')

class Francia:
    def capital(self):
        print('Paris')
    
    def language(self):
        print('French')

colombian = Colombia()
frenchs = Francia()

for country in (colombian,frenchs):
    country.capital()
    country.language()

#------------------------------------ Polymorphism whit herency ------------------------------------------------

class Birds:
    def fly(self):
        print('The majority of the birds can fly but some cant')

class Eagles(Birds):
    def fly(self):
        print('The eagles can fly')

class Hens(Birds):
    def fly(self):
        print('The hen cant fly')

new_bird = Birds()
new_eagle = Eagles()
new_hen = Hens()
new_bird.fly()
new_eagle.fly()
new_hen.fly()