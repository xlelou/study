#!/usr/bin/env ptython
#coding:utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

fanme = raw_input('enter fiel name:')

try:
    fobj = open(fanme,'r')
except IOError,e:
    print e
else:
    for eachLine in fobj:
        print eachLine
    fobj.close()