# Map:
# With map, you pass in a transformer function which takes one item and transforms it into its new value.
# When each item is transformed we say that the operation is a mapping,
# or just a map of the original list.
# list = map(<some transformer function>, <some list with variables to iterate over>)

# Filter:
# When some items are omitted, we call it a filter.
# list = filter(<filteration function>, <some list with variables to iterate over>)
# With filter, you pass in a filtration function which takes an item and returns a boolean. True if the item should be included, false if the item should be filtered out.
# The function provides a list like object and thus needs to be converted to a list


# List comprehension:
# yourlist = [value * 2 for value in list] this will double the values in the list
# [<transformer expression> for <variable name> in <sequence> if <fiteration expression>]
def longlenghts(strings):
    return [len(s) for s in strings if len(s) >= 4]
print(longlenghts(['a','bc','def','ghij','klmno']))
def longlenghts(strings):
    filter_strings = filter(lambda s: len(s) >= 4,  strings)
    return map(lambda s: len(s) , filter_strings)
print(list(longlenghts(['a','bc','def','ghij','klmno'])))

tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
inner_list = tester['info']
compri = [d['name'] for d in inner_list]
print(compri)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print([x*2 for x in lst if x % 2 == 0])
lst = filter(lambda i: i % 2 == 0, lst)
print(list(map(lambda x: 2*x, lst)))


x = lambda a,b: a*b
print(x(3,7))

def myfunc(n):
    return lambda a : a*n
mymultp = myfunc(5)
print(mymultp(3))

abbrevs = []
for i in range(0,9): abbrevs.append(str(input("please enter the text and make it easier for me!!!: ")))
print(list(map(lambda a:a.upper(), abbrevs)))