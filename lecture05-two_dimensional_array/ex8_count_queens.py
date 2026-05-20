def  isQueen(a,i,j,n):
      value=a[i][j]
      for x in range(n):
            if a[i][x]>value:
                  return False
      for y in range(n):
            if a[y][j]>value:
                  return False
      r,c=i,j
      while r>=0 and c>=0:
            if a[r][c]>value:
                  return False
            r-=1
            c-=1
      r,c=i,j
      while r>=0 and c<n:
            if a[r][c]>value:
                  return False
            r-=1
            c+=1
      r,c=i,j
      while r<n and c>=0:
            if a[r][c]>value:
                  return False
            r+=1
            c-=1
      r,c=i,j
      while r<n and c<n:
            if a[r][c]>value:
                  return False
            r+=1
            c+=1
      return True
n=int(input())
a=[]
for i in range(n):
    t=list(map(int,input().split()))
    a.append(t)
count=0
for i in range(n):
      for j in range(n):
            if isQueen(a,i,j,n)==True:
                  count+=1
print(count)