#/usr/bin/python
#Learning Python :)
#http://www.pythonchallenge.com/pc/def/linkedlists.php

import urllib
import re

counter = 0
newvar = 0
parameter = {'nothing':'12345'}
params = urllib.urlencode(parameter)
pattern = re.compile('and the next nothing [0-9].*')

while counter < 400:
	result = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?%s" % params)
	inquery = result.read()
	print "Page: \n%s" % inquery
	stringed = re.findall(pattern, inquery)
	print stringed[0]
	if stringed[0] == '16044':
		stringed[0] = '8022'
		newvar = stringed[0]
	elif stringed[0] == '82683':
		stringed[0] = '63579'
		newvar = stringed[0]
	else:
		newvar = stringed[0]
	params = urllib.urlencode({'nothing':newvar})
	parameter['nothing'] = newvar
	counter += 1