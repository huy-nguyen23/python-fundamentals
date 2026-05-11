m,n=map(int,input().split())
a=[]
for i in range(m):
    t=list(map(int,input().split()))
    a.append(t)
for i in range(m):
      sum_m=0    
      for j in range(n):
            sum_m+=a[i][j]
      print(f'{i}: {sum_m}')