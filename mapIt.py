#! python3
# -*- coding: utf-8 -*-
#title					:mapIt.py
#author					:Debashmita
#date of creation		:11/07/2022 13:57
#==============================================================================
#runs fine 

import webbrowser,sys,pyperclip as pc

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pc.paste()
    
webbrowser.open('https://www.google.com/maps/place/' + address)