#!/usr/bin/env python
# coding:utf8
import sys
import os



reload(sys)
sys.setdefaultencoding('utf8')


# 编辑文件部分 没写出来


ls = os.linesep
#编写文件
def make():
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


#读取文件
def read():

    fanme = raw_input('enter fiel name:')

    try:
        fobj = open(fanme,'r')
    except IOError,e:
        print e
    else:
        for eachLine in fobj:
            print eachLine.strip()
        fobj.close()
def begin():
    print '''
        1.make
        2.read
        3.exit
'''

begin()
select = raw_input('enter num:')



if select == '1':
    make()
elif select =='2':
    read()
else:
    exit()
