import webbrowser, sys, pyperclip
#Very simple script that simple searches google maps for a location
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
webbrowser.open('https://www.google.co.uk/maps/search/'+address)
