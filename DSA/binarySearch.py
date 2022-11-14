#iterative

def binarySearch(arr,item):
    low = 0
    high = len(arr)-1
    while low<high:
        mid = (low+high)//2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            high = mid -1
        elif arr[mid] < item:
            low = mid + 1
    return -1

# print("The index pos found is ",binarySearch([3,6,45,89,100,122,189,19999],189))

def recursiveBS(arr,item,low,high):
    if low > high:
        return False
    else:
        mid = (low+high) //2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return recursiveBS(arr,item,low,mid-1)
        elif arr[mid] < item:
            return recursiveBS(arr,item,mid+1,high)
    return -1


# print("The index pos found is ",binarySearch([3,6,45,89,100,122,189,19999],122))