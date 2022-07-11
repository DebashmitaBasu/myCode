#! python3
# -*- coding: utf-8 -*-
#title                  :header4NewFile.py
#author                 :Debashmita
#date of creation		:10/07/2022 11:00
#==============================================================================
#Creates this Description and opens the created file in VSCode

# Import the modules needed to run the script.
import os
from os.path import exists
from time import strftime

div = '======================================='

def select_editor():
    print("Opening the file VSCode editor.")
    os.system("code " + title)
    exit()

def createTitle(t):
    t = t.title()
    t = t[0].lower() + t[1:]  
    t = t + '.py'
    t = t.replace(' ', '')
    return t

def writeHeader(fName,author,date):
    fName.write('#! python3')
    fName.write('\n# -*- coding: utf-8 -*-')
    fName.write('\n#title\t\t\t\t\t:' + title)
    fName.write('\n#author\t\t\t\t\t:' + author)
    fName.write('\n#date of creation\t\t:' + date)
    fName.write('\n#' + div * 2 + '\n')
    fName.write('\n')

def createHeaderVars():
    name = "Debashmita"
    date = strftime("%d/%m/%Y %H:%M")
    return name, date

if __name__ == "__main__":
    title = createTitle(input("Enter a title for your script: "))

    # Check to see if the file exists to not overwrite it.
    if exists(title):
        print("\nA script with this name already exists.")
        filename = open(title, 'r+')
        firstPart = filename.read()
        if not firstPart.startswith("#! python3\n# -*- coding: utf-8 -*-\n#title"):
            #print(firstPart)
            filename.seek(0)
            name, date = createHeaderVars()
            writeHeader(filename, name, date)
            filename.write(firstPart)
        
    else:
        filename = open(title, 'w')
        name, date = createHeaderVars()
        writeHeader(filename, name, date)

    filename.close()

    select_editor()
