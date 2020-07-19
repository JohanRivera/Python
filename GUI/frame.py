#Importamos la libreria
from tkinter import * 

raiz = Tk() #Iniciamos a utlizar la libreria por defecto para interfaz gráfica de python
raiz.title("Ventana de prueba") #Modificar nombre de la ventana
raiz.resizable(True,True) #Modificar tamaño de ventana cuando ya este creado (ancho, alto), entonces, 
#si colocamos False bloqueamos la opción de poner más grande la ventana, y true para permitirlo
raiz.iconbitmap('C://Users//johan//OneDrive//Documentos//GitHub//Python//GUI//icon.ico') #Modificar icono de la ventana

#El frame es con lo que vamos a trabajar al interior de la ventana.

myFrame = Frame(raiz,width='650', height='350' ) #instanciamos para utilizar el frame
#Tambien se le puede cambiar el borde a las pestañas con .config(bd=10), el número es editable dependiendo el 
#tamaño, y este se puede combinar con .config(relief="sunken") o =groove
#Además con .config(cursos='hand2'), se puede cambiar el aspecto del cursor
myFrame.pack(fill='both',expand='True') #Se empaqueta el frame con la raiz, que sería la ventana, adentro, tiene
#la opción de saber en que dirección va a crecer el frame y en si se expande o no. 

"""Adicionalmente en el frame se puden utilizar los labels los cuales son utilizados"""
myImage = PhotoImage(file="C://Users//johan//OneDrive//Documentos//GitHub//Python//GUI//homer.gif")
#Esta librería unicamente lee archivos GIF y PGM
#myLabel = Label(myFrame, text = 'Hellow World!')
Label(myFrame,image=myImage).place(x=100, y=200)
#myLabel.place(x=100, y=200) #Este .place es para seleccionar en que parte de la pantalla va a salir el msj
#no es necesario utilizar el .pack o no va a funcional el .place y vicebersa
#myLabel.pack() #Siempre que se utiliza el .pack es para empaquetar lo que estamos utilizando con todo lo que 
#hemos realizado con anterioridad
raiz.mainloop() #Abrir una ventana, este debe ser la última sentencia para que los cambios seas efectuados