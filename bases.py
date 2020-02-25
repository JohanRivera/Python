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
lista = [] #Primera forma de declarar una lista
lista2 = list() #Segunda forma de decalrar una lista
#Ejemplo
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
diccionario = dict() #Forma de declarar un diccionario 1
diccionario2 = {} #Forma de declarar un diccionario 2

diccionario = {
    'johan' : 22,
    'felipe' : 23,
    'saludo' : "hola"
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

#Funciones
def funct1():
    print("Mi primera función")

def funct2(x='Valor por defecto'): #Le puedo dar valores por defecto a cualquier variable que no seciba un valor.
    print(x)

#Estructurar el codigo mediante una función principal
if __name__ == '__main__':
    funct1()
    funct2()


