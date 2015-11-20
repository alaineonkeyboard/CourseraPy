fname = raw_input("Enter file name: ")
fh = open('romeo.txt')

lst = list()

for line in fh:
    print line
    words = line.split()
    print words
    for word in words:
        print word
        if word in lst: continue
        lst.append(word)

print lst.sort()
