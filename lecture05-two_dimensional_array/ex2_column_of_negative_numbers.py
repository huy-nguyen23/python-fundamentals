m,n=map(int,input().split())
a=[]
for i in range(m):
    t=list(map(int,input().split()))
    a.append(t)
for j in range(n):
      flag=False
      for i in range(m):
            if a[i][j]>0:
                  flag=True
                  break
      if flag==False:
             print(j,end=' ')