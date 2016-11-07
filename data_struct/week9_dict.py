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
    lst.append(words[1])
print lst

# var2 Add key: value in dict
counts = dict()
for nemail in lst:
    counts[nemail] = counts.get(nemail,0) + 1
print counts

# count to big value
bigmail = None
bigcount = None
for email,count in counts.items():
    if bigcount == None or count > bigcount:
        bigcount = count
        bigmail = email
print bigmail, bigcount

# var 1
# for name in lst:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] = counts[name] +1
# print counts
