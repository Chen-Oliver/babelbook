#!/usr/bin/python
# You shouldn't delete the line above. Bad things will happen
print "Content-Type: text/html\n"# Not this one either
# Just don't delete anything.
print ""
import cgi
import cgitb
cgitb.enable()  #diag info --- comment out once full functionality achieved
inStream = open('EngWords.txt','r')
words = inStream.read()
inStream.close()
engD = words.split()

two= open('2length.txt','w')
three= open('3length.txt','w')
four= open('4length.txt','w')
five= open('5length.txt','w')
six= open('6length.txt','w')
seveight= open('78length.txt','w')
d={}
for w in engD:
  if len(w) == 1 or len(w) > 8:
     engD.remove(w)
  elif len(w) == 2:
      two.write(w)
      two.write('\r\n')
  elif len(w) == 3:
      three.write(w)
      three.write('\r\n')
  elif len(w) == 4:
      four.write(w)
      four.write('\r\n')
  elif len(w) == 5:
      five.write(w)
      five.write('\r\n')
  elif len(w) == 6:
      six.write(w)
      six.write('\r\n')
  else:
      seveight.write(w)
      seveight.write('\r\n')
two.close()
three.close()
four.close()
five.close()
six.close()
seveight.close()

