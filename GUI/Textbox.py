from tkinter import *
raiz = Tk()
myFrame = Frame(raiz, width=800, height=400)
myFrame.pack()

textBox = Entry(myFrame)
textBox.grid(row=0,column=1) #grid is for controlate all using rows and columns 
#Further, in .grid(row=0, column=1, sticky='e', padx=50) the comand padx o pady move the object, in this case
#50 pixels to este, this direction can changed with the comand sticky
#Besides, the color and others features of the text box can changed
passBox = Entry(myFrame)
passBox.grid(row=1,column=1)
passBox.config(show='*')#this line is for changed the characters with a character special
""" Text Box to comments"""
commentsBox = Text(myFrame,width=10,height=5) #Form to create the comment box
commentsBox.grid(row=2,column=1) 
scrollVertical = Scrollbar(myFrame,command=commentsBox.yview) # Form to make a scroll in the comment box 
scrollVertical.grid(row=2,column=2,sticky='nsew') # the command nsew is what the scroll it have the same size
#that comment box
commentsBox.config(yscrollcommand=scrollVertical.set) #For the scroll 


myLabel = Label(myFrame, text = 'Ingrese el nombre: ')
myLabel.grid(row=0,column=0) #grid is for controlate all using rows and columns 
myPass = Label(myFrame, text = 'Ingrese contraseña: ')
myPass.grid(row=1,column=0)
myComments = Label(myFrame, text = 'Comentarios: ')
myComments.grid(row=2,column=0)

raiz.mainloop()