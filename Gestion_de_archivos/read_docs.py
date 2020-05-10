#------------------------------- TEXT DOCS ------------------------------------------------------------------
#NOTE The document students.txt is will to use the examples shows in this explanation
"""
Open and close of documents
The function is open('filename','mode')
The modes are: 
    ‘r’ – Read mode which is used when the file is only being read 
    ‘w’ – Write mode which is used to edit and write new information to the file 
          (any existing files with the same name will be erased when this mode is activated) 
    ‘a’ – Appending mode, which is used to add new data to the end of the file; that is new
          information is automatically amended to the end 
    ‘r+’– Special read and write mode, which is used to handle both actions when working with a file

Important note: The route of compile should is in the route of document if only we use the name of the file
                on the contrary we need put all de route in te paramater 'filename' of the function open()
"""
#--------------------------------- USE OF MODE 'r' ------------------------------------------------------
"""
To open a document only with the name of document is:
      docs_students = open('students.txt','r') 

To open a document with the route complete is:
      docs_students = open('C://Users//johan//OneDrive//Documentos//GitHub//Python//Gestion_de_archivos//students.txt','r')

The functions which we can use are:
      *readable() - This function use a boolean to tell us if is possible to read the document, the form to 
                    use the function is:
                        print(docs_students.readable())

      *read() - Function to read the document, the form to use the function is:
                        print(docs_students.read()) 
      
      *readline() - Read the firts line of document, but if we use the function again this return the next line
                    the form to use the function is:
                        print(docs_students.readline()) 

      *readlines() - Read all the document and return a list with the lines of document, the form to use the
                     the function is: 
                        print(docs_students.readlines())
                     Too we can access to a position of this list:
                        print(docs_students.readlines()[1]) 

When we use this functions leave the document without information that read and if we use 
again this function or a 'for' to read the document, it seems that is empty, for example:
      for i in docs_students:
            print(i) #This line print all the lines of document
      print(docs_students.readlines()) #But in this line return a list empty
other example is:
      print(docs_students.read()) #This line print all the lines of document
      print(docs_students.read())#But in this line return anything empty
      

To end is necessary close the document, thus, to this action we use the function 
docs_students.close() #So close a document

"""

# ------------------------------------------ USE OF MODE 'w' --------------------------------------------
"""
To create a document only with the name of document this is create in the same binder the executed python doc:
      docs_students = open('students2.txt','w') 

To create a document in a route specific is:
      docs_students = open('C://Users//johan//OneDrive//Documentos//GitHub//Python//Gestion_de_archivos//students2.txt','w')

The functions which we can use is:
      *write() - The function write in the document, for example:
            docs_students2.write('Hello, this is a new document \n and we can write anything.')

With this mode we only can overwrite the document, for example, if the document have the word 'hello' and 
we use the function write() to write 'and how are you?' on the document this in overwrite only with 'and how 
are you' and the word that there was is erase. For example:
      docs_students2.write('Hello')
      print(docs_students2.read())
      docs_students2.write('and how are you')
      print(docs_students2.read())

To end is necessary close the document, thus, to this action we use the function 
docs_students.close() #So close a document
"""

# ------------------------------------------ USE OF MODE 'a' --------------------------------------------
"""
To open a document only with the name of document is:
      docs_students = open('students.txt','a') 

To open a document with the route complete is:
      docs_students = open('C://Users//johan//OneDrive//Documentos//GitHub//Python//Gestion_de_archivos//students.txt','a')

Now, for adds information the document is necesary use the funtion write(), a example would:
      docs_student.write('\nSe adiciona esta parte')
      print(docs_students.read())

To end is necessary close the document, thus, to this action we use the function 
docs_students.close() #So close a document
"""

#------------------------------------- ERASE DOCUMENTS ----------------------------------------------
"""
Is necesary use the library os, the example is:
      
      import os
      #To erase the document only with the name of document is:
      os.remove('students2.txt') 
      #To erase a document with the route complete is:
      os.remove('C://Users//johan//OneDrive//Documentos//GitHub//Python//Gestion_de_archivos//students2.txt')

"""