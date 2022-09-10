fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    for word in line.split():
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)



fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
        x = line.split()
        print(x[1])
        count = count+1
print("There were", count, "lines in the file with From as the first word")
