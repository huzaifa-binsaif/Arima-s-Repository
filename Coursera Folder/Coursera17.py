dict = {}
data = 'marquard zhen csev\nzhen cwen marquard\nzhen csev cwen\nzhen csev marquard\n'
print(data)
names = data.split()
for name in names:
    dict[name] = dict.get(name, 0) + 1
# for key in dict:
    # print(key+':', dict[key])
for key, value in dict.items():
    print(key+':', value)
bigcount = None
bigword = None
for word, count in dict.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word
print('')
print('biggest word is:', bigword, 'and it was repeated', bigcount, 'times!')

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
        dict[x[1]] = dict.get(x[1], 0) + 1

bigcount = None
bigword = None
for word, count in dict.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word
print(bigword, bigcount)
