""""
9.4 Write a program to read through the mbox-short.txt and figure out who has
the sent the greatest number of mail messages. The program looks for 'From ' lines
and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count
of the number of times they appear in the file. After the dictionary is produced,
the program reads through the dictionary using a maximum loop to find the most
prolific committer.
"""

#name = raw_input("Enter file:")
name = "mbox-short.txt"

if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
# test  = handle.read() # just a text

# Parsing log file to find line which begins from "From "
lst = list()
for line in handle:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    lst.append(words[5])
#print lst

h_lst = list()
for i in lst:
    #print i
    h = i.split(":")
    h_lst.append(h[0])
#print h_lst

counts = dict()
for nemail in h_lst:
    counts[nemail] = counts.get(nemail,0) + 1
#print counts

new_time = list()
for key, val in counts.items():
    new_time.append( (key, val) )
#print new_time

new_time.sort()
for key, val in new_time:
    print key, val