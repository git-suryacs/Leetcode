def rotate(arr,n):
    d =1
    while d<=n:
        last = arr[0]
        for i in range(n-1):
            arr[i] = arr[i+1]
        d+=1
print(rotate([1,2,3,4,5,6,7],3))