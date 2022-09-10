
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    total = total + float(line[21:])
    count = count+1
average  = total/count
print('Average spam confidence:',average)
