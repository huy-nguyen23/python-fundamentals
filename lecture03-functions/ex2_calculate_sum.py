def tongSum(n):
  sum=0
  for i in range(1,n+1):
    sum+=i**2
  return sum
n=int(input())
a=tongSum(n)
print(a)