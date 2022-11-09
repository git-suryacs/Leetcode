# def binarySearch(a,n,item):
#     low = 0
#     high = n -1
#     while (low<=high):
#         mid = (low+high)//2
#         if (a[mid]) == item :
#             return mid
#         elif(a[mid]<item):
#             low = mid+1
#         else:
#             high= mid-1
    
#     return -1

def binarySearch(a,n,item):
    low = 0
    high = n-1
    while (low <= high):
        mid = (low+high)//2
        if a[mid] == item:
            return mid
        elif a[mid] < item:
            low = mid+1
        else:
            high = mid -1
    return -1


print(binarySearch([5,7,2,1,9,13],6,9))



