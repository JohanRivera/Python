from tkinter import *
raiz = Tk()
myFrame = Frame(raiz, width=800, height=400)
myFrame.pack()
myName = StringVar()
option = IntVar()

textBox = Entry(myFrame, text=myName)
textBox.grid(row=0,column=1) #grid is for controlate all using rows and columns 
#Further, in .grid(row=0, column=1, sticky='e', padx=50) the comand padx o pady move the object, in this case
#50 pixels to este, this direction can changed with the comand sticky
#Besides, the color and others features of the text box can changed
passBox = Entry(myFrame)
passBox.grid(row=1,column=1)
passBox.config(show='*')#this line is for changed the characters with a character special

myLabel = Label(myFrame, text = 'Ingrese el nombre: ')
myLabel.grid(row=0,column=0) #grid is for controlate all using rows and columns 
myPass = Label(myFrame, text = 'Ingrese contraseña: ')
myPass.grid(row=1,column=0)

def codeButton():
    if option.get() == 1: # set or get
       labelPrint.config(text = 'Bienvenido ' + textBox.get()) 
       labelPrint.pack()
    else: 
        labelPrint.config(text = 'Bienvenida ' + textBox.get())
        labelPrint.pack()

labelPrint = Label(raiz)
Radiobutton(raiz, text='Male', variable=option, value=1).pack() #Create an option to select
Radiobutton(raiz, text='Female', variable=option, value=2).pack() #Create an option to select
buttonSend = Button(raiz, text='Enviar', command = codeButton) #Create a button
buttonSend.pack()

raiz.mainloop()