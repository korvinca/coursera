fname = "mbox-short.txt"
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    words = line.split()
    # print 'Debug:', words
    # if line == "" : continue
    # if len(words) < 1 : continue
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    try:
        count = count + 1
        print words[1]
    except:
        print 'Index out of range.'
        break

print "There were", count, "lines in the file with From as the first word"

