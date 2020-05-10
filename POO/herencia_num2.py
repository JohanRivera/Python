"""
Inicialmente se inicia creando la clase principal Persona, la cual tiene como atributos el nombre y la edad.
Estos atributos son llenados mediante el uso de la función '__init__()' la cual se ejecutará al momento de 
crear un objeto o una instancia de esta clase. Adicionalmente, la clase principal Persona cuenta con un 
metodo que me imprime cuando se desee los valores de los atributos de esta clase. 
"""
class Persona: 
    def __init__(self, name, age): #Metodo para definir los valores de los atributos de la clase
        self.nombre = name #Asigna el valor de name al atributo nombre
        self.edad = age #Asigna el valor de age al atributo edad
    def imprimir(self): #Metodo para imprimir cuando yo deseo los atributos de la clase
        print(f'Esta persona se llama {self.nombre} y su edad es {self.edad}') #Imprimir los parametros de la clase

"""
Ahora, se crea una subclase de la clase principal la cual es llamada Empleado, esta subclase añade un atributo
el cual es sueldo. Adicionalmente, se crea un metodo el cual mediante el uso del atributo sueldo dice si el
empleado debe o no pagar impuestos (para pagar impuestos el sueldo debe ser mayor a 3000).
"""
class Empleado(Persona):
    def __init__(self, name, age, salary):#Metodo para definir los valores de los atributos de la subclase
        Persona.__init__(self, name, age)#Esta linea utiliza el metodo __init__() de la clase principal
        #para llenar en la subclase los dos atributos que se heredaron de la clase principal.
        self.sueldo = salary#Asigna el valor de salary al atributo sueldo que pertence unicamente a la subclase 
    def impuesto(self):#Metodo que nos dice si el empleado debe o no pagar impuestos
        if self.sueldo > 3000: #Se utiliza un if el cual observa si el valor del atributo sueldo es mayor a
            #3000, dado el caso que esta comparación sea verdadera el empleado debera pagar impuesto
            print(f'El empleado {self.nombre} tiene que pagar impuestos')#Imprime que el empleado debe pagar
        else:#Dado el caso que la comparación del if sea falsa el empleado no debera pagar impuesto
            print(f'El empleado {self.nombre} no tiene que pagar impuestos')#Implrime que el empleado no debe pagar

"""
Se crea un objeto o instancia de la clase Persona, con el atributo de nombre = 'Johan' y con el atributo de 
edad = 20. Adicionalmente, se utiliza el metodo imprimir de esta clase para mostrar por pantalla el valor
de estos atributos.
"""
newPerson = Persona('Johan',20)#Creación del nuevo objeto
newPerson.imprimir() #Imprime atributos

"""
Se crea un objeto o instancia de la subclase Empleado llamado newEmployed, con el atributo de nombre = 'Leandro', el atributo de 
edad = 20 y el atributo sueldo = 2000. Adicionalmente, se utiliza el metodo impuesto de esta subclase para 
mostrar por pantalla que el empleado no debe pagar impuestos debido que su sueldo es menor a 3000
"""

newEmployed = Empleado('Leandro',20,2000)
newEmployed.imprimir()
newEmployed.impuesto()

"""
Se crea un objeto o instancia de la subclase Empleado llamado newEmployed2, con el atributo de nombre = 'Rivera', el atributo de 
edad = 20 y el atributo sueldo = 3001. Adicionalmente, se utiliza el metodo impuesto de esta subclase para 
mostrar por pantalla que el empleado debe pagar impuestos debido que su sueldo es mayor a 3000
"""

newEmployed2 = Empleado('Rivera',20,3001)
newEmployed2.imprimir()
newEmployed2.impuesto()