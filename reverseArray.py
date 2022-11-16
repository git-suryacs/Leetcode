def reverseArray(A,low,high):

    while low < high:
        A[low],A[high] = A[high],A[low]
        low+=1
        high-=1
    return A

A = [1, 2, 3, 4, 5, 6]
print(A)
reverseArray(A, 0, 5)
print("Reversed list is")
print(A)