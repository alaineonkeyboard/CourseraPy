import urllib

fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

'''for line in fhand:
	print line.strip()'''


print type(fhand)