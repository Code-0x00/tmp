#!/usr/bin/python
#coding=utf-8
# Import modules for CGI handling
import cgi, os
import cgitb; cgitb.enable()
import os
import os.path


#import facedetectme
form = cgi.FieldStorage()
# Get filename here.
fileitem = form['up_file']
# Test if the file was uploaded
if fileitem.filename:
	fn = os.path.basename(fileitem.filename)
	open('/home/xhq/XhqServer/Upload/' + fn, 'wb').write(fileitem.file.read())
	message = 'The file "' + fn + '" was uploaded successfully'
else:
	message = 'No file was uploaded'


rootdir = '/home/xhq/XhqServer/Upload'

str_files='files list:<br/>'
for parent,dirnames,filenames in os.walk(rootdir):
	
	for filename in filenames:
		filelink='<a href=http://192.168.1.102:2333/Upload/'+filename+'>'+filename+'</a><br>'
		str_files=str_files+filelink
		#str_files=str_files+filename+'<br/>'

sstr="""\
	 Content-Type: text/html\n

	 <html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><title>Share</title><style type="text/css">
article{
		-webkit-column-count: 2;
		-webkit-column-gap: 21px;
		-moz-column-count: 2;
		-moz-column-gap: 21px;
		column-count: 2;
		column-gap: 21px;
		}
	h1 {
		text-align: center;
		-webkit-column-span: all;
		-moz-column-span: all;
		column-span: all;
		}
	p {
		margin-top: 0px;
		margin-bottom: 12px;
		}
	footer{
		-webkit-column-span:all;
		-moz-column-span:all;
		column-span:all;
		}

	table,tr, td, th {
		border: 1px soild black;
		border-collapse: collapse;
		padding: 3px;
		}
	</style></head><body><br>

	<h1 style="text-align: center" class="first">Share<br></h1><hr>
	<form action="http://192.168.1.102:2333/cgi-bin/server.py" method="post" enctype="multipart/form-data">
		<input type="submit" name="submit" value="Submit Files" /> <a > <a/> <input name="up_file" type="file" name="file" id="file" /><br>
	</form>
	<hr>
%s
<hr>
</body><div></div></html>
"""%(str_files)
print sstr