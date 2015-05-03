#/usr/bin/python
#Learning Python :)
#http://www.pythonchallenge.com/pc/def/ocr.html
myarray = []

f = open('challenge_3.txt').read()
mylist = map(list, f)

for char in mylist:
	if char not in myarray:
		myarray.append(char)
		print mylist.count(char)
		print char
