#------------------------------- TEXT DOCS ------------------------------------------------------------------
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
"""

docs_students = open('..\\students.txt','r') #So open a document
print(docs_students.readable()) #This function use a boolean to tell us if is possible to read the document
docs_students.close() #So close a document