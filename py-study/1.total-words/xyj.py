#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import sys 
reload(sys)
sys.setdefaultencoding('utf8')

fr = open('xyj.txt','r')

charters = []

stat = {}

for line in fr:
	line = line.strip()

	if len(line) == 0:
		continue
	
	line = unicode(line)
	
	for x in xrange(0, len(line)):
		if not line[x] in charters:
			charters.append(line[x])

		if not stat.has_key(line[x]):
			stat[line[x]] = 0
		stat[line[x]] +=1

fr.close()
for key, value in stat.items():
	print key, value


stat = sorted(stat.iteritems(), key=lambda d:d[1], reverse=True)

print type(stat)

