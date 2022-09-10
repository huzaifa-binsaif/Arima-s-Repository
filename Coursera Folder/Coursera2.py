def test() :
    values = [4, 7, 8, 9, -5]

    if values[-1] < 0:
        values.pop(-1)
    average = 0
    sum = values[0] + values[1]
    average = sum/2
    values.insert(1,average)
    temp = 0
    temp = values[0]
    values[0] = values[-1]
    values[-1] = temp

    print(values)
    return values


test()
