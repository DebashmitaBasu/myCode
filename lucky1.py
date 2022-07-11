#! python3
# it's working! :D
import sys, webbrowser

'''if len(sys.argv) < 2:
    print("The pattern is:- lucky.py <search term>")
    sys.exit()'''

searchTerm = ' '.join(sys.argv[1:])
webbrowser.open('https://www.google.com/search?q=' + searchTerm)
