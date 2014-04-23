# -*- coding: utf-8 -*-
"""
Created on Fri Feb 07 12:09:19 2014

@author: Kris
"""

import imaplib
import re
import urllib2
import zipfile
import cgi

#Email Information
account = "cs460zipdump@gmail.com"
password = "Class-Test-2014"

#Login to gmail and enter inbox
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(account, password)
mail.list()
mail.select("inbox")

#Grab Email Bodies
charset, data = mail.uid('search', None, "ALL")
recentUnreadID = data[0].split()[-1]
charset, data = mail.uid('fetch', recentUnreadID, '(RFC822)')
raw_mail = data[0][1]

#Regex to parse out URLs
x = re.compile(r"http://(\w*[.])*(\w*/)*(\w*[-]\w*)*[?](\w*[-]\w*)*")
 
url = x.search(raw_mail).group()
print url

#Open URL and grab filename
zfile = urllib2.urlopen(url)
_,params = cgi.parse_header(zfile.headers.get('Content-Disposition', ''))
filename = params['filename']

#Download the file
print "Beginning File Download\n"
data = zfile.read()
with open(filename, "wb") as code:
    code.write(data)
print "Download Complete\n"

#Unzip the file
with zipfile.ZipFile(filename, "r") as z:
    z.extractall()

#Upload the file to vxcage

#Upload the file to virus total

#Upload the file to totalhash


