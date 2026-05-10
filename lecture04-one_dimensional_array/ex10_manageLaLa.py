n=int(input())
a=list(map(int,input().split()))
count=0
flag=True
for x in a:
      if x==0:
             count+=1
      if count>3:
            flag=False
            break
      if x==1:
            count=0
if a[n-1]==1 and flag==True:
      print('YES')
else:
      print('NO')