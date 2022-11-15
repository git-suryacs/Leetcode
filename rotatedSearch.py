def pivotedBinarySearch(arr1,n,key):
    pivot = findpivot(arr1,0,n-1)
    if pivot == -1:
        return binarySearch(arr1,0,n-1,key)
    if arr1[pivot] == key:
        return pivot

    if arr1[0] <=key:
        return binarySearch(arr1,0,pivot-1,key)
    return binarySearch(arr1,pivot+1,n-1,key)

def findpivot(arr1,low,high):
    if low > high:
        return -1
    elif low == high:
        return low

    mid = (low+high)//2
    if mid < high and arr1[mid] > arr1[mid+1]:
        return mid
    elif mid > low and arr1[mid-1]>arr1[mid]:
        return mid-1
    elif arr1[low] > arr1[mid]:
        return findpivot(arr1,low,mid-1)
    else:
        return findpivot(arr1,mid+1,high)



def binarySearch(arr1,low,high,item):
    if low > high:
        return False
    else:
        mid = (low+high)//2
        if arr1[mid] == item:
            return mid
        elif arr1[mid] > item:
            return binarySearch(arr1,low,mid-1,item)
        elif arr1[mid] < item:
            return binarySearch(arr1,mid+1,high,item)




if __name__ == '__main__':
    arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    n = len(arr1)
    key = 3
    print("Index of the element is : ", pivotedBinarySearch(arr1, n, key))