def primeNumbers(n):
      if n<2:
            return False
      else:
            for i in range(2,n):
                  if n%i==0:
                        return False
            return True
n=int(input())
a=[]
count=0
for i in range(n):
      t=list(map(int,input().split()))
      a.append(t)
for i in range(n):
      if primeNumbers(a[i][i])==True:
            count+=1
print(count)