m,n=map(int,input().split())
a,b,p=map(int,input().split())
for i in range(m):
    for j in range(n):
        print(a,end=' ')
        newNum=(a+b)%p
        a=b
        b=newNum
    print()