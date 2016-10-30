# Use words.txt as the file name
#fname = raw_input("Enter file name: ")

fname = open('words.txt')
for line in fname:
    line = line.rstrip().upper()
    print line
