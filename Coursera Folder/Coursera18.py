c = {'a': 10, 'b': 1, 'c': 22}
temp = []
def takeSecond(tuple):
    return tuple[1]
for key,value in c.items():
    temp.append((key, value))
# print(temp)
temp.sort(key = takeSecond,reverse=True)
# print(temp)
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = 0
dict = {}
for line in handle:
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
        x = line.split()
        x = x.split(':')
        dict[x[0]] = dict.get(x[0], 0) + 1
print(dict)


# The apporved code
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = 0
dict = {}
for line in handle:
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
        x = line.split()
        x = x[5].split(':')
        dict[x[0]] = dict.get(x[0], 0) + 1
temp = []
for key,value in dict.items():
    temp.append((key, value))
temp.sort()
for key,value in temp:
    print (key,value)
