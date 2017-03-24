#!/usr/bin/python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')


fr = open('text.txt','r')
charters = []

stat = {}




for line in fr:
	#qu kongge 
	line = line.strip()

	if len(line) == 0:
		#ruguo kong hang ,go on
		continue

	line = unicode(line)

	for x in xrange(0, len(line)):
		#mei hang meiyou zhege zi  charu shuzu 
		if not line[x] in charters:
			charters.append(line[x])
		#zidianzhong cun zai yici  jia 1
		if not stat.has_key(line[x]):
			stat[line[x]] = 0
		stat[line[x]] += 1

fr.close()

stat = sorted(stat.items(), key = lambda d:d[1], reverse = False)
#gen ju zhi pailie

for x in xrange(0, 5):
	print charters[x]
	#dayinchu hou 5ge 

for key, value in stat:
	print key, value


