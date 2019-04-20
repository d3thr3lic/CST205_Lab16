#CST 205 - Lab 16
#Mitchell Saunders
#Nicholas Saunders

import urllib

def openURL():
  #pulls and opens webpage
  sock = urllib.urlopen("http://www.cnn.com/US/OJ/")
  #reads and saves sock
  htmlTxt = sock.read()
  #closes website
  sock.close()
  
  #grab the Ul tag within htmlTxt
  ulSection = extractUL(htmlTxt)
  #Convert strings in the UL tag to list elements 
  elementList = collectStories(ulSection)
  #formats list elements into a HTML formatted String
  htmlStrOfList = makeHtmlStrFromList(elementList)
  #save content as HTML file
  makePage(htmlStrOfList)
  
  
def makeHtmlStrFromList(elementList):
  htmlStr = ""
  openTag = "<li>"
  endTag = "</li>"
  #goes through each element in list 
  #and appends elements into string that is HTMLized in a <li>
  for element in elementList:
    htmlStr = htmlStr + openTag + element + endTag
  return htmlStr

def extractUL(htmlTxt):
  firstTag = "<ul>"
  lastTag = "</ul>"
  #goes through HTMLtxt and finds beinging and ending tags of <ul>
  firstTagLocation = htmlTxt.lower().find(firstTag)
  secondTagLocation = htmlTxt.lower().find(lastTag)
  
  #pulls strings between <ul> and </ul>
  excerpt = htmlTxt[firstTagLocation + len(firstTag):secondTagLocation]
  return excerpt

def collectStories(htmlTxt):
  fileTxt = htmlTxt
  
  startListTag = "<li>"
  endHeaderTag = "</a>"
  
  lastLocation = 0
  elementList = []
  listTxt = ""
  
  #loop through string containing all list elements 
  #and extracts one list element at a time
  while fileTxt.find(startListTag, lastLocation) != -1:
    #finds start of desired string and appends to an element list
    locationOfTag = fileTxt.lower().find(startListTag, lastLocation)
    endOfHeaderLocation = fileTxt.lower().find(endHeaderTag, locationOfTag)
    locOfRtCarrot = fileTxt.find(">",locationOfTag + len(startListTag))
    headerTxt = fileTxt[locOfRtCarrot + 1:endOfHeaderLocation]
    elementList.append(headerTxt)
    lastLocation = locationOfTag + 1
  
  return(elementList)

def makePage(htmlStr):
  setMediaPathToCurrentDir()
  #replace the directory in the line below with the path to your file
  file = open(getMediaPath() + "superweb.html", "wt")
  file.write("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 
  Transition//EN" "http://www.w3.org/TR/html4/loose.dtd">
  
  # passes htmlstr with <h3> tags 
  #and passes each element into the HTML file and saves
  <html>
  <head><title>I made this page with Python!</title>
  </head>
  <body>
  """ + htmlStr + """
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
