# cook your dish here
if __name__ =='__main__':
    T = int(input())
    for i in range(0,T):
        X,Y,K,N = map(int,input().split())
        Lucky = False
        for j in range(0,N):
            P,C = map(int,input().split())
            pagesNeeded = X - Y
            if pagesNeeded <= P and K >=C:
                Lucky = True
        if Lucky :
            print('LuckyChef')
        else:
            print('UnluckyChef')
            
    
    