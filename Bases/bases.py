a = "hola"
b = 5
c = 3.3 
d = True
print (type(a), type(b), type(c), type(d))
c = True
print('\n', type(c))
b = "mundo"
saludo = a + b
print(saludo)


#OPERADORES
b = 5
c = 3.3
print(b+c)
print(b-c)
print(b*c)
print(b/c)
print(b//c) # aproximación para darun entero
print(b**c) # potencia 
print(b%c) # modulo

print(b and c)
print(b or c)

#Secuencia de datos. Vectores
#Estructuras de datos
#1. Listas
#Las listas como son objetos pueden almacenar cualquier variable.
#Las listas se pueden recorrer de manera positvia y negativa, por ejemplo, tenemos una 
#lista n=['hola', 'nooo','bb'], y llamamos a n[-1] estamos llamando al ultimo valor de la lista que es 'bb',
# y así sucesivamente.
#Para eliminar un elemento de una lista, sigamos con la lista n del comentario anterior, y escribimos
# del n[1]; en ese momento estamos eliminando la segunda posicion de la lista que es 'nooo'. Adicionalmente,
# también se puede eliminar un elemento de una lista utilizando la función remove la cual se utiliza
# escribiendo literalmente el cual elemento se desea borrar, utilizando la misma lista n sería:
# n.remove('hola'), y eliminaría justo el elemento que se esta escribiendo.


lista = [] #Primera forma de declarar una lista
lista2 = list() #Segunda forma de decalrar una lista
#Ejemplo
#Otra forma para añadir elementos a una lista, es especificando en cual posición deseo que el 
# nuevo elemento se añada mediante la función insert, siguiendo con la lista n del ejemplo, quedaría:
# n.insert(0, 'adios'), en este ejemplo la lista quedaría así: n = ['adios', 'hola', 'nooo', 'bb']

lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)
lista.append('Hola')
lista.append(7)
for i in lista: #El i es realmente un apuntador en un arreglo dinamico.
    print(i)

#Rangos
for j in range(10): #Cuando se utiliza rango, funciona para arrojarme la posición de un vector
    print(j)

#Tuplas
#Es un vector estatico, al declararla se vuelve inmutable.
Tupla = ('Hola', 1, 2, 6.7) #Forma de declararlo
print(Tupla) #Al imprimir una tupla se observa en parentesis
print(lista) # Y al imprimir una lista se observa entre corchetes cuadrados

print(type(lista), type(Tupla))

#Diccionario
#Un diccionario es un vector que se almacena por parejas, en donde le primer valor esla lave "key" y el segundo valor 
#es el contenido o el valor. NOTA: LA LLAVE NO SE PUEDEN REPETIR.
#Para agregar nuevos elementos al diccionario seria, diccionario['amarillo'] = 'yellow'
#Para eliminar es mediante el uso de del la cual sería, del(diccionario['amarillo'])
#Adicionalmente, puedo dentro de un diccionario utilizar otro diccionario  o lista ejemplo:
# diccionario = {'Johan':{'edad' : 22, 'estatura' : 170 cm}, 'Pedro':[23, 170 cm]}
#Una forma para llamar un diccionario y que no salga error si no encuentra la llave se utiliza el metodo get
# el cual se usa así: print(diccionario.get{'Johan', 'No existe esta clave en el diccionario'}),
# entonces dado el caso que no exista esa clave va a salir el msj que se dejo predeterminado de lo contrario
# saldra el valor que tendra esa clave
#Una forma para saber si una clave existe dentro de un diccionario es utilizando: 'Johan' in diccionario
# esa instrucción nos arrojara un valor booleano, True si existe y False si no existe. 
#Además, para mostrar unicamente las claves del diccionario se utiliza el metodo keys que sería:
# print(diccionario.keys()). Y si en caso contrario solo quieres saber los valores se utiliza el metodo values
# que sería: print(diccionario.values()), y si se quiere saber ambas cosas se puede utilizar el metodo items o
# sencillamante llamar al diccionario, que sería: print(diccionario.items()) o print(diccionario)
#Por otro lado, si se desea ver cuantos elementos tiene mi diccionario se utiliza el metodo len
# que sería: len(equipo), esto nos indica numericamente cuantos elementos tiene mi diccionario 
#Por último, si se desea eliminar todo el diccionario se ejecutaría el metodo clear: 
# diccionario.clear()

diccionario = dict() #Forma de declarar un diccionario 1
diccionario2 = {} #Forma de declarar un diccionario 2

diccionario = {
    'johan' : 22,
    'felipe' : 23,
    'saludo' : "hola",
}

for key in diccionario:
    print("llave: ", key, " contenido: ", diccionario[key])

#Conjuntos
#set, es un set al igual que en los diccionarios las variables no se pueden repetir.
listaprueba = [1,1,2,2,3,3,4,4]
print(listaprueba)
listaprueba = set(listaprueba) #El set lo utilizamos en algun vector para eliminar variables repetidas.
print(listaprueba)

dset = {1,2,3,4,5,'hola',1}
print(dset)


#Sentencias
#Condicionales
var1 = 1
var2 = 10
#Condicionales anidados
if var1 == var2:
    print('Es igual')
elif var1 > var2:
    print('Es mayor var1')
else:
    print('No sirve')

#ciclos
for x in 'hola':#Recorre la palabra, letra por letra
    print(x)
else: #Funciona para cuando acabe el ciclo hacer una acción inmediata
    print('hola')

j=0
while j < 10:
    j+=1
    print(j)
else:  #Funciona para cuando acabe el ciclo hacer una acción inmediata
    print("Se salio prro")

#Funciones regulares, se pueden llamar a si mismas dentro de la función.
def holaMundo():
    print("Hola mundo")

def suma(x=0,y=0): #Le puedo dar valores por defecto a cualquier variable que no seciba un valor.
    return x+y

def ParOImpar(x):
    return (x%2 == 0)

#A continuación se puede ver como se hace el manejo de errores en las funciones para que el programa 
# no se salga porque encuentra un error, sino que siga ejecutando si no es grave
import random

def genNumAleatorio(min,max): #Función que genera un numero aleatorio entre un rango
    try:
        if min > max:
            return random.randint(max,min)
        return random.randint(min,max)
    except TypeError:
        print("Debes escribir numeros")
        return -1 

def factorial(num):
    try:
        resultado = num
        for i in range(num-1,1,-1):
            resultado *= i
        return resultado
    except TypeError:
        print("Debes escribir un numero")
        return -1 

def numerosEntre(a,b):
    try:
        if a>b:
            cambio = a
            a = b
            b = cambio
        for i in range(a+1,b):
            print(i)
    except TypeError:
        print("Debes escribir un numero")
        return -1 

#Funciones Lambdas, estas funciones lambdas son funciones de una linea de codigo las cuales pueden recibir 
#la cantidad de parametros que se desee desde 0 hasta infinito.
flambda = lambda a, b, c, d: a*b/c+d-10
print(flambda(10,20,50,100))

#Slides
nombre = "Leandro"

print(nombre[0])
print(nombre[0:3])
print(nombre[:3])
print(nombre[3:])
print(nombre[1:7:2])#Coger la variable guardada y imprimir o guardar desde la posicion 1 del vector hasta la posicion 7 pero en pasos de dos
print(nombre[::-1])#Retorna todo el vector al revez

#Estructurar el codigo mediante una función principal
if __name__ == '__main__':
    holaMundo()
    suma(10,10)
    ParOImpar(11)


