fh = raw_input('Enter file name: ')
if len(fh) < 1 :
    fh = open('mbox-short.txt')
fsm = 0
fstr = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count_sm = line.split(" ")
    f = float(count_sm[1])
    fsm = fsm + f
    fstr = fstr + 1
asm = fsm / fstr
print "Average spam confidence:", asm
