#/usr/bin/python
#Learning Python :)
#http://www.pythonchallenge.com/pc/def/map.html
import string

#Read the file
#Print the file
#For each char in line, add two to ascii value
#print
def main():
	f = open('challenge_2.txt').readlines()
	lis = map(list, f)

	for a in range(0, len(lis[0])):
		#print get_ascii_value(lis[0][a])
		print convert(get_ascii_value(lis[0][a]))

def get_ascii_value(character):
	chars = []
	alphabet = string.ascii_lowercase
	for a in alphabet:
		chars.append(a)

	for num in range(0, len(chars)):
		if chars[num] == character:
			return num
	
def convert(character):
	chars = []
	alphabet = string.ascii_lowercase

	for a in alphabet:
		chars.append(a)

	if character == 24:
		return chars[0]
	elif character == 25:
		return chars[1]
	elif character == None:
		return ""
	else: 
		return chars[character+2]

main()