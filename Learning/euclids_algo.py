def GCD(a,b):
    while b!=0:
        t = a
        a = b
        b = t%b
    return a


print(GCD(20,8))
