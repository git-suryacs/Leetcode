# def fact(n):
#     factAnswer = 1
#     if n == 0 or n ==1:
#         return 1
#     else:
#         while n >1:
#             factAnswer *=n
#             n-=1
#     return factAnswer



# print(fact(10))

# def rfact(n):
#     if n>=1:
#         return n * rfact(n-1)
#     elif n ==0:
#         return 1
#     else:
#         return "Value is not suitable"

# print(rfact(10))


def fact(n):
    factAns = 1
    while (n!=0):
        factAns = n * factAns
        n-=1
    return factAns
# print(fact(5))


def rFact(n):
    if n < 0:
        return "sorry"
    if n == 0:
        return 1
    else:
        return rFact(n-1) * n

print(rFact(-5))