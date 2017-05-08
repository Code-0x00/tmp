#!/usr/bin/python
#coding=utf-8
# Import modules for CGI handling
import cgi, os
import cgitb; cgitb.enable()
import os
import os.path
import sys
reload(sys)
sys.setdefaultencoding('utf8')


rootdir = '/home/xhq/XhqServer/web/upload/'
#import facedetectme
form = cgi.FieldStorage()
# Get filename here.
try:
        fileitem = form['up_file']
        # Test if the file was uploaded
        if fileitem.filename:
                fn = os.path.basename(fileitem.filename)
                open(rootdir + fn, 'wb').write(fileitem.file.read())
                message = 'The file "' + fn + '" was uploaded successfully'

except:
        message='index'
#delete files
try:
        debug0=form['a']
        ct=debug0.value
        for parent,dirnames,filenames in os.walk(rootdir):
                filename=filenames[int(ct)]
                os.remove(rootdir+filename)
except:
        message = 'No file was uploaded'




str_files="""<hr/>"""
for parent,dirnames,filenames in os.walk(rootdir):
        countfile=0
        for filename_t in filenames:
                filename=''
                for i in filename_t:
                        if i==' ':
                                filename+='%20'
                        else:
                                filename+=i
                filelink='<a href=http://192.168.1.102:2334/Upload/'+filename+'>'+filename_t+'</a>'
                delete_str="""<a href=http://192.168.1.102:2334/cgi-bin/upload.py?a=%s>[delete]</a>"""%(str(countfile))
                str_files=str_files+delete_str+'&nbsp&nbsp'+filelink+'<br>'
                countfile+=1


sstr="""\
         Content-Type: text/html\n

         <html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><title>Submit Files</title><style type="text/css">

        </style></head><body><br>

        <h1 style="text-align: center" class="first">Submit Files<br></h1>
        <form action="upload.py" method="post" enctype="multipart/form-data">
                <input type="submit" name="submit" value="Submit Files" /> <a > <a/> <input name="up_file" type="file" name="file" id="file" /><br>
        </form>
        
%s

</body><div></div></html>
"""%(str_files)
print sstr
