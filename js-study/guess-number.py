# -*- coding: UTF-8 -*-
import random

secert = random.randint(1,100)
guess = 0
tries = 0

while guess != secert and tries <6:
	guess = input('guess num')
	if guess < secert:
		print 'too little'
	elif guess > secert:
		print 'too big'
	tries = tries + 1
if guess == secert:
	print 'right'
else:
	print 'no chance'