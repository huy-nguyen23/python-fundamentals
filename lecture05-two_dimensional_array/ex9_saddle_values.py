def saddlePoints(i,j,a,m,n):
      value=a[i][j]
      for x in range(n):
            if a[i][x]>value:
                  return False
      for y in range(m):
            if a[y][j]<value:
                  return False
      return True
m,n=map(int,input().split())
a=[]
for i in range(m):
    t=list(map(int,input().split()))
    a.append(t)
count=0
for i in range(m):
      for j in range(n):
            if saddlePoints(i,j,a,m,n)==True:
                  count+=1
print(count)