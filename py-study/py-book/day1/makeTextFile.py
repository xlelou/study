#!/usr/bin/env python
# coding:utf8
import sys
import os

reload(sys)
sys.setdefaultencoding('utf8')

ls = os.linesep

fname = raw_input('enter the name:')

while True:
    if os.path.exists(fname):
        print "error: '%s' already exists" % fname
        break
    else:
        break

all = []

print "enter '.' means quit"

while True:
    entry = raw_input('>')
    if entry == '.':
        break
    else:
        all.append(entry)

fobj = open(fname,'w')
fobj.writelines(['%s %s' % (x,ls)for x in all])
fobj.close()
print 'well done'
