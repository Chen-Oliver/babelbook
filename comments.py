#!/usr/bin/python
# You shouldn't delete the line above. Bad things will happen
print "Content-Type: text/html\n"# Not this one either
# Just don't delete anything.
print ""
import cgi
import cgitb
cgitb.enable()
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
keys=d.keys()
try:
 comments = d[keys[0]] + '<br><hr><br>'
except:
 comments = 'User forgot to give your awesome feedback :|<br><hr><br>'
comment = open('comments.html','a')
comment.write(comments)
comment.close()

print '<meta HTTP-EQUIV="REFRESH" content="0; url=comments.html">'
print "<center>Secret: Sometimes when I'm home alone I like to dig a hole in my back yard and pretend to be a carrot. <br> P.S: You should'nt be seeing this</center>"
