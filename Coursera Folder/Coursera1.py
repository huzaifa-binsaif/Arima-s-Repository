file = input('enter the file name: ')
file = open(file, 'r')
x = file.read()
occurrences = 0
keyword = str(input('please enter keyword: '))
a = int(input('how many synonyms would you like to enter?: '))
synonym = list(range(0,a+1))
for i in range (0,a+1):
    if i == 0:
        synonym[i] = keyword
    else:
        synonym[i] = str(input('please enter synonym: '))
for i in range (0,a+1):
    occurrences = occurrences + x.count(synonym[i])
print("The number of times the keyword and its synonyms were used in the document are: ", occurrences)
