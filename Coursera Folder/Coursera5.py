def verify(number) : # do not change this line!
    list = [0,1,2,3,5,6,7,8,10,11,12,13]
    total = 0
    for item in range(0,12):
        total = total + int(number[list[item]])
    sum = int(number[0]+number[1]) + int(number[7]+number[8])
    if int(number[0]) != 4:
        return '1'
    elif int(number[3])-1 != int(number[5]):
        return '2'
    elif total % 4 != 0:
        return '3'
    elif sum != 100:
        return '4'
    else:
        return True # modify this line as needed
input ="4094-3460-2754" # change this as you test your function
output = verify(input) # invoke the method using a test input
print(output) # prints the output of the function
# do not remove this line!
