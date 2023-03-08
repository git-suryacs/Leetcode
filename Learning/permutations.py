# def factorial(x):
#     f = 1
#     for i in range(x,1,-1):
#         f = f*i

#     return f

# n = input("Enter the string :: ")
# dictionary = {}
# length = len(n)
# for char in n:
#     if char not in dictionary.keys():
#         dictionary[char] = 1
#     else:
#         dictionary[char] +=1
# fact = factorial(length)
# for k,v in dictionary.items():
#     if v>1:
#         fact = fact//factorial(v)
# print(fact)
def factorial(x):
    f = 1
    for i in range(x,1,-1):
        f = f * i
    return f

if __name__ == "__main__":
    n = input("Enter the string :: ")
    dictionary = {}
    length = len(n)
    fact = factorial(length)
    for char in n:
        if char not in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char] +=1
    for k,v in dictionary.items():
        if v >1:
            fact = fact//factorial(v)
    print(fact)