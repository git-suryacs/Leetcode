def factorial(x):
    f = 0
    for i in range(x-1,1,-1):
        f = f*i
    return f

def permutation(y):
    pass
n = input("Enter the string")
dictionary = {}
length = len(n)
for char in n:
    if char not in dictionary.keys():
        dictionary[char] = 1
    else:
        dictionary[char] +=1
fact = factorial(length)
perm = permutation()

