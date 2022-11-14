# def fib(n):
#     n1,n2 = 0,1
#     if n ==0:
#         print("Enter Valid number")
#     else:
#         while n!=0:
#             print(n1)
#             nth = n1 + n2
#             n1 = n2
#             n2 = nth
#             n-=1

# fib(10)

#recursive

def rFib(n):
    if n <= 1:
        return n
    else:
        return (rFib(n-1)+rFib(n-2))

for i in range(0,10):
    print(rFib(i))

