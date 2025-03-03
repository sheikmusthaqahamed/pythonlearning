import os

print(os.sep)  #\

print(os.path.join("cognizantgithub","pythonlearning")) #cognizantgithub\pythonlearning

print(os.getcwd())  #Current Working Directory  #C:\Users\2157925\Downloads\cognizantgithub\pythonlearning

print(os.path.abspath(r"File_Handling\file_handling.py"))  #C:\Users\2157925\Downloads\cognizantgithub\pythonlearning\File_Handling\file_handling.py

print(os.path.dirname(os.getcwd()))   #C:\Users\2157925\Downloads\cognizantgithub

print(os.path.basename(os.getcwd()))  #pythonlearning

print(os.path.relpath(r"C:\Users\2157925\Downloads\cognizantgithub\pythonlearning\File_Handling\file_handling.py")) #File_Handling\file_handling.py\

print(os.path.abspath("file_handling.py"))  #C:\Users\2157925\Downloads\cognizantgithub\pythonlearning\file_handling.py

print(os.path.expanduser("~file_handling.py")) #C:\Users\file_handling.py

print(os.path.abspath("../../testData/"))  #C:\Users\2157925\Downloads\testData

