# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print "Error opening file"
    exit()

totalval = 0
average = 0
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    startpos = line.find(":") + 1
    count += 1
    totalval += float(line[startpos:])
    
print totalval / count
