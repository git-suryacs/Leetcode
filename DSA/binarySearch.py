# # Iterative
# def binarySearch(arr,item):
#     low = 0 
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low+high)//2
#         if arr[mid] == item:
#             return mid
#         elif arr[mid] < item :
#             low = mid+1
#         else:
#             high = mid-1
#     return -1



# arr = [10,3,1,8,36,25,25]
# item = 3
# res= binarySearch(arr,item)
# print("the index is ",res)

# # time complexity - O(log n)
# # space complexity - O(1)


# Recursion
def BS(arr,item,low,high):
    if low > high :
        return False
    else:
        mid = (low+high)//2
        if item == arr[mid]:
            return mid
        elif(item < arr[mid]):
            return BS(arr,item,low,mid-1)
        else:
            return BS(arr,item,mid-1,high)
    
print("recursive BS - > ",BS([15,21,47,84,96],84,0,5))
