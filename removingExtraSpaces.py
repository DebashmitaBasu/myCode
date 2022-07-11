#! python3
# -*- coding: utf-8 -*-
#title					:removingExtraSpaces.py
#author					:Debashmita
#date of creation		:11/07/2022 14:30
#==============================================================================
#runs :D

import pyperclip as pc

text = pc.paste()
newList=[]

text = text.split('\n')
for i in range(len(text)):
    newList.append(text[i].strip())
text = ' '.join(newList)

pc.copy(text)
withoutSpaces = open('withoutSpacesNew1.txt','w')
withoutSpaces.write(text)
withoutSpaces.close()
print("Extra Spaces Removed! Check the clipboard & file!")