#Menu and emergents windows

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

raiz = Tk()
barMenu = Menu(raiz)
raiz.config(menu=barMenu, width=300, height=300)

def informationAditional():
    messagebox.showinfo("We are the future", 'Software 2020')

def errorWindow():
    messagebox.showerror("Error", 'dll.xd 235')

def warningWindow():
    messagebox.showwarning('Restriction','You are breaking rules')

def exitApp():
    value=messagebox.askquestion('Exit','Are you sure that you want to exit?')
    if value == 'yes':
        raiz.destroy()

"""Further, askokcancel is similar to askquestion, the principal different is that askquestion set 'Yes' or 'Not'
and the values that set are 'yes' or 'not', but, askokcancel set 'Ok' or 'Cancel' and theirs values are 
true and false.

Besides, tambien exist askretrycancel
"""

def openArchive():
    archive = filedialog.askopenfilename(title='Open', initialdir='/', filetypes=(("Fichero de excel",'.xlsx'),('Fichero de texto','.txt')))
    print(archive)

archiveMenu = Menu(barMenu, tearoff=0)
archiveMenu.add_command(label='New')
archiveMenu.add_command(label='open',command=openArchive)
archiveMenu.add_command(label='Save', command=warningWindow)
archiveMenu.add_command(label='Save as')
archiveMenu.add_separator()
archiveMenu.add_command(label='Exit',command=exitApp)

editMenu = Menu(barMenu, tearoff=0)
editMenu.add_command(label="Copy")
editMenu.add_command(label="Cut")
editMenu.add_command(label="Paste", command=errorWindow)

toolMenu = Menu(barMenu, tearoff=0)
toolMenu.add_command(label='Modify')

helpMenu = Menu(barMenu, tearoff=0)
helpMenu.add_command(label='About of...', command=informationAditional)

barMenu.add_cascade(label='Archive', menu=archiveMenu)
barMenu.add_cascade(label='Edit', menu=editMenu)
barMenu.add_cascade(label='Tools', menu=toolMenu)
barMenu.add_cascade(label='Help', menu=helpMenu)

raiz.mainloop()