#/usr/bin/python
#Learning Python :)
#http://www.pythonchallenge.com/pc/def/equality.html

import re

f = open('challenge_4.txt').read()
pattern = re.compile('[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}')
result = re.findall(pattern, f)
little = re.compile('[a-z]')
for string in result:
	answer = re.findall(little, string)
	print answer[1]