import re

f = open('regex_sum_182228.txt', 'r')
total = 0

for line in f:
	lst = re.findall('[0-9]+', line)
	if len(lst) > 0:
		for x in lst:
			total += float(x)

print int(total)