import urllib
#warmup
def openURL():
  sock = urllib.urlopen("http://www.cnn.com/US/OJ/")
  #print(sock.read())
  htmlTxt = sock.read()
  sock.close()
  
  subesetHtml = collectStories(htmlTxt)
  

def collectStories(htmlTxt):
  

def makePage():
  setMediaPathToCurrentDir()
  #replace the directory in the line below with the path to your file
  file = open(getMediaPath() + "superweb.html", "wt")
  file.write("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 
  Transition//EN" "http://www.w3.org/TR/html4/loose.dtd">
  
  <html>
  <head><title>I made this page with Python!</title>
  </head>
  <body>
  <h1>MY PYTHON PAGE!!!</h1>
  </body>
  </html>""")
  
  file.close()
  


#to allow mediaPath to be correct an linux, macos and windows.
def setMediaPathToCurrentDir():
  fullPathToFile = os.path.abspath(__file__)
  if fullPathToFile.startswith('/'):
    setMediaPath(os.path.dirname(fullPathToFile))
  else:
    setMediaPath(os.path.dirname(fullPathToFile) + '\\')
