def maxN (n):
    soLonNhat=0
    while n>0:
        chuSO=n%10
        if soLonNhat<chuSO:
            soLonNhat=chuSO
        n//=10
    return soLonNhat
n=int(input())
a=maxN(n)
print(a)