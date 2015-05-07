#/usr/bin/python
#Learning Python :)
#http://www.pythonchallenge.com/pc/def/linkedlists.php

import urllib
import re

counter = 0
newvar = 0
parameter = {'nothing':'12345'}
params = urllib.urlencode(parameter)
pattern = re.compile('and the next nothing is [0-9].*')
new_pattern = re.compile('[0-9].*')

while counter < 400:
	result = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?%s" % params)
	inquery = result.read()
	print "Page: \n%s" % inquery
	stringed = re.findall(pattern, inquery)
	new_stringed = re.findall(new_pattern, stringed[0])
	print stringed
	print stringed[0]
	if new_stringed[0] == '16044':
		new_stringed[0] = '8022'
		newvar = new_stringed[0]
	#elif stringed[0] == '82683':
	#	stringed[0] = '63579'
	#	newvar = new_stringed[0]
	else:
		newvar = new_stringed[0]
	params = urllib.urlencode({'nothing':newvar})
	parameter['nothing'] = newvar
	counter += 1