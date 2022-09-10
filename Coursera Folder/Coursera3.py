def test() : # do not change this line!
  list = [4, 5, 1, 9, -2, 0, 3, -5] # do not change this line!
  min1 = list[0]
  min2 = list[1]
  lenght = len(list)
  for item in range(2,lenght):
      if list[item] < min1:
          if min1 < min2:
              min2 = list[item]
          else:
              min1 = list[item]
      else:
          if list[item] < min2:
              min2 = list[item]


  print(min1, min2)
  return (min1, min2) # do not change this line!
# do not write any code below here

test() # do not change this line!
# do not remove this line!
