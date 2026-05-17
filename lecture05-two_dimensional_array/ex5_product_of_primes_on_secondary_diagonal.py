def primeNumbers(n):
      if n<2:
            return False
      else:
            for i in range(2,n):
                  if n%i==0:
                        return False
            return True
v=int(input())
a=[]
product=1
for i in range(v):
      t=list(map(int,input().split()))
      a.append(t)
for i in range(v):
      if primeNumbers(a[i][v-1-i])==True:
            product*=a[i][v-1-i]
print(product%1000003)