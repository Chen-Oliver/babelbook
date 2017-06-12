#!/usr/bin/python
# You shouldn't delete the line above. Bad things will happen
print "Content-Type: text/html\n"# Not this one either
# Just don't delete anything.
print ""
# If there are less than 3 lines excluding the warnings, cry, because now you must find
# out what must be retyped, and that requires work
print "<!DOCTYPE html>"
print "<html>" # don't delete this either
inStream = open('EngWords.txt','r')
words = inStream.read()
inStream.close()
x = words.split()
d={}
for w in x:
  if len(w) == 1 or len(w) > 8:
     x.remove(w)
  else:
     d[w] = 1
print d
