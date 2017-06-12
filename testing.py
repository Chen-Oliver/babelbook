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
print "<center><h1>Randomly Generated Gibberish</h1></center>"
import cgi
import cgitb
#cgitb.enable()  #diag info --- comment out once full functionality achieved
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
inStream = open('EngWords.txt','r')
words = inStream.read()
inStream.close()
engD = words.split()
d={}
for w in engD:
  if len(w) == 1 or len(w) > 8:
     engD.remove(w)
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
                text.replace(word,'<mark>' + word +'<mark>')
    return text
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
    return counts(line)

def book():
    b= ''
    for n in range(410):
        page = lines(80,40,userL)
        b += '<center><pre>'
        b += page
        b += '</pre></center>'
        b += "<h4><center>Page "+str(n+1)+"</h4><center><br><br>"
    return b

    
print book() 
print '<link rel="stylesheet" type="text/css" href="styles.css">'
print "</html>" 

