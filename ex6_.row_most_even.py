def evenNumbers(n):
    if n%2==0:
        return True
    else:
        return False
m,n=map(int,input().split())
a=[]
for i in range(m):
    t=list(map(int,input().split()))
    a.append(t)
index=0
max_count=0
for i in range(m):
    count=0
    for j in range(n):
      if evenNumbers(a[i][j])==True:
         count+=1
    if max_count<count:
      max_count=count
      index=i
print(index)