import re
file = open('GET_actual_data.txt','r')
x = file.read()
y = re.findall('[0-9]+',x)
print(len(y))
total = 0
for i in range(0,len(y)):
    total = total + int(y[i])
print(total)


import re
print( sum( [ int(i) for i in re.findall('[0-9]+', open('GET_actual_data.txt','r').read()) ] ) )
