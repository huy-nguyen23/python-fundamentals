n=int(input())
a=list(map(int,input().split()))
max=a[0]
for x in a:
      if max<x:
              max=x
print(max)