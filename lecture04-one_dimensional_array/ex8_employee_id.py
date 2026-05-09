def employeeID():
    n=int(input())
    a=list(map(int,input().split()))
    msnv=[False]*100001
    for x in a:
        msnv[x]=True
    for i in range(1,100001):
        if msnv[i]==False:
            return i
a=employeeID()
print(a)