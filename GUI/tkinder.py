"""Cuando se utiliza esta libreria el programa con la extensión .py, se abre dos ventanas una tipo consola y 
la otra que es la que queremos, para esto se crea un archivo con extensión .pyw"""
#Importamos la libreria
from tkinter import * 

raiz = Tk() #Iniciamos a utlizar la libreria por defecto para interfaz gráfica de python
raiz.title("Ventana de prueba") #Modificar nombre de la ventana
raiz.resizable(False,False) #Modificar tamaño de ventana cuando ya este creado (ancho, alto), entonces, 
#si colocamos False bloqueamos la opción de poner más grande la ventana, y true para permitirlo
raiz.iconbitmap('C://Users//johan//OneDrive//Documentos//GitHub//Python//GUI//icon.ico') #Modificar icono de la ventana
raiz.geometry('650x350')#Ancho x alto
raiz.config(bg='blue') #Cambiar opciones de la pantalla, como color.
raiz.mainloop() #Abrir una ventana, este debe ser la última sentencia para que los cambios seas efectuados


