#!/usr/bin/python
# You shouldn't delete the line above. Bad things will happen
print "Content-Type: text/html\n"# Not this one either
# Just don't delete anything.
print ""
# If there are less than 3 lines excluding the warnings, cry, because now you must find
# out what must be retyped, and that requires work
print "<!DOCTYPE html>"
print "<html>" # don't delete this either
print "<title>Gibberish</title>"
print "<font color = 'LightCoral'><center><h1>Randomly Generated Book</h1></center></font>"
print "<a name='TOP'><body>"
import cgi
import cgitb
cgitb.enable()  #diag info --- comment out once full functionality achieved
import random
import urllib #used this module to decode encoded characters in the url
def FStoD():
    '''
    Converts cgi.FieldStorage() return value into a standard dictionary
    '''
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d
d=FStoD()

try:
 if 'plen' in d:
    userL=float(d['plen'])
 elif 'length' in d:
    userL=float(d['length'])
 else:
    userL = 40
except:
    userL = 40
try:
    userC = urllib.unquote(d['chars'])
except:
    userC =''

LBAlph= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
     ',',' ','.','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
LBPunct= [', ', '. ', ' ']
if 'alpha' in d:
    if d['alpha'] == 'yes':
        LBAlph += userC.split(',')
    if d['alpha'] == 'no':
        LBAlph = userC.split(',')
else:
    LBAlph = userC.split(',') 

#inStream = open('EngWords.txt','r')
#words = inStream.read()
#inStream.close()
#engD = words.split() #was orginally used to get list of all words 
wD={}
userWL = d['wlen']
fileN = str(userWL) + 'length.txt'
inStream = open(fileN,'r')
userWords = inStream.read()
inStream.close()
engD = userWords.split()
#for w in engD:
 # if len(w) == 1 or len(w) > 8:
 #    engD.remove(w)
def probs():
    x = 100
    if x >= 0:
        if random.randrange(101)<x:
            x-=2
            return True
        else:
           x = 100
           return False
    else:
        x=100
        return False
def counts(text):
    text = text.split(' ')
    for n in engD:
        for word in text:
            if n in word:
                if n not in wD:
                    wD[n] = 1
                else:
                    wD[n] +=1
    return wD
def lines(length,linesL,userL):
    line = ''
    if int(userL) == linesL:
        for l in range(linesL):
            for n in range(length):
                if probs():
                    line += str(LBAlph[random.randrange(len(LBAlph))])
                else:
                    line += str(LBPunct[random.randrange(3)])
            if l == 0:
                line = '<p>' + line +'<br><br>'
            if l == 39:
                line += '</p>'
            if l != 0 and l!= 39:
                line += '<br><br>'
    else:
        for l in range(int(userL)):
            for n in range(length):
                if probs():
                    line += str(LBAlph[random.randrange(len(LBAlph))])
                else:
                    line += str(LBPunct[random.randrange(3)])
            if l == 0:
                line ='<p>' + line + '<br><br>'                
            if l == userL - 1:
                line += '</p>'                
            if l != 0 and l!= userL-1:
                line +='<br><br>'
    return line,counts(line)

def book():
    b= ''
    both = lines(80,40,userL)
    b += '<center><pre>'
    b += "<a href='index.html' style = 'float:left' > Go Back Home </a><br>"
    b += "<a href='#BOT' style = 'float:left' > Check out the Word Table! </a><br>"
    b += both[0]
    wD.update(both[1])
    b += '</pre></center>'
    b += "<h4><center>Page 1 </h4><center><br><br>"
    for n in range(409):
        both = lines(80,40,userL)
        b += '<center><pre>'
        b += both[0]
        wD.update(both[1])
        b += '</pre></center>'
        b += "<h4><center>Page "+str(n+2)+"</h4><center><br><br>"
    return b
print book()
def keyFind(val):
  for w in wD:
    if wD[w] == val:
        return w
def wordOcc():
    counter = 0
    vals = wD.values()
    valL = len(vals)
    if valL >= 30:
       retStr ="<center><pre> <font size =10 color=LightCoral>Top 30 Words </font></pre></center>" + \
        '<table border = 1>' + '<th> Ranking</th>' + '<th> Word </th>'+'<th> Frequency </th>'\
        + '<th> Google Definition </th>'
            
       while counter < 30:
          m = max(wD.values())
          k = keyFind(m)
          counter += 1
          retStr += "<tr><td>"+ str(counter) + "</td><td>" + str(k) + "</td><td>"+ str(m) + \
                    "</td><td>" + "<a target='_blank' href='https://www.google.com/#safe=strict&q="+ str(k)+"+definition'>" + "Definition</a>"+"</td></tr>"
          wD.pop(k)
       return '<pre>' + retStr + '</pre>'
    else:
       retStr ="<center><pre> <font size =10 color=LightCoral>All " + str(valL) + " Words </font></pre></center>" + \
          '<table border = 1>' + '<th> Ranking</th>' + '<th> Word </th>'+'<th> Frequency </th>'\
        + '<th> Google Definition </th>'
        
       while counter < len(vals):
          m = max(wD.values())
          k = keyFind(m)
          counter += 1
          retStr += "<tr><td>"+ str(counter) + "</td><td>" + str(k) + "</td><td>"+ str(m) + \
                    "</td><td>" + "<a target='_blank'href='https://www.google.com/#safe=strict&q="+ str(k)+"+definition'>" + "Definition</a>"+"</td></tr>"
          wD.pop(k)
       return '<center><pre>' + retStr + '</pre></center>'

print wordOcc()
print "<a name='BOT'></body>"
print "<a href='index.html' class='home' style = 'float:left' color ='LightCoral'> Go Back Home </a><br>"
print '<link rel="stylesheet" type="text/css" href="styles.css">'
print "<a href='#TOP' class='botL'color ='LightCoral'> Go Back Top </a><br>"
print "</html>" 


