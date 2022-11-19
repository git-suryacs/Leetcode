# cook your dish here


if __name__ == '__main__':
    T = int(input())
    for i in range(0,T):
        N,C = map(int,input().split())
        A = list(map(int, input().split()))
        Sum = sum(A)
        if C - Sum >= 0:
            print("Yes")
        else:
            print("No")