# Zipping lists together:

L1 = [3,4,5]
L2 = [1,2,3]
L3 = []
for i in range(len(L1)):
    L3.append(L1[i] + L2[i])
print(L3)

# Using the zip function:
L5 = []
L4 = list(zip(L1,L2))
#for (x1, x2) in L4:
    #L5.append(x1+x2)
print(L4)

L5 = [x1+x2 for (x1, x2) in list(zip(L1,L2))]# can alos use L4
print(L5)
L6 = []
L6 = map(lambda x: x[0] + x[1], zip(L1, L2))
print(list(L6))
# Example program for guesses made in hangman:
def possible(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for i in range(len(word)):
        bc = blanked[i]
        wc = word[i]
        if bc == '_' and wc in guesses_made:
            return False
        elif bc != '_' and bc != wc:
            return False
    return True

print(possible("wonderwall", "_on__r__ll", "otnqurl"))
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))

# Same example using zip function:
def possible(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for (bc, wc) in zip(blanked, word):
        if bc == '_' and wc in guesses_made:
            return False
        elif bc != '_' and bc != wc:
            return False
    return True

print(possible("wonderwall", "_on__r__ll", "otnqurl"))
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))

# Test question
A1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
A2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

A3 = [ x1+x2 for (x1,x2) in zip(A1,A2) if x1 > 10 and x2 < 5]
print(A3)

# Simplifying the Example program for guesses made in hangman
def compatible_char(bc,wc,guesses_made):
    if bc == '_' and wc in guesses_made:
        return False
    elif bc != '_' and bc != wc:
        return False
    else:
        return True

def possible(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for (bc,wc) in zip(blanked,word):
        if not compatible_char(bc,wc,guesses_made):
            return False
    return True

print(possible("wonderwall", "_on__r__ll", "otnqurl"))
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))
