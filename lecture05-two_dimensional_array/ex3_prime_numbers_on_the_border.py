def primeNumbers(n):
      if n<2:
            return False
      else:
            for i in range(2,n):
                  if n%i==0:
                        return False
            return True
m,n=map(int,input().split())
a=[]
count=0
for i in range(m):
      t=list(map(int,input().split()))
      a.append(t)
for j in range(n):
      if primeNumbers(a[0][j])==True:
            count+=1
      if primeNumbers(a[m-1][j])==True:
            count+=1
for i in range(m):
      if i==0 or i==m-1:
            continue
      if primeNumbers(a[i][0])==True:
            count+=1
      if primeNumbers(a[i][n-1])==True:
            count+=1
print(count)