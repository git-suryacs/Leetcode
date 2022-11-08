number = int(input("Enter the number of items"))
list = []
for i in range(0,number):
    list.append(int(input("Enter item")))

print(list)

smallest = list[0]
for i in range(1,len(list)):
    if list[i] < smallest:
        smallest = list[i]


print(smallest)


# time complexity : O(N)