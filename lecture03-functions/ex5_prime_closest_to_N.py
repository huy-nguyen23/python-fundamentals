def soNguyenTo(n):
  if n<2:
    return False
  else:
    for i in range(2,n):
      if n%i==0:
        return False
    return True
n=int(input())
a=soNguyenTo(n)
if a==True:
  print(n)
else:
  t=1
  while True:
    if soNguyenTo(n-t)==True:
        print(n-t)
        break
    elif soNguyenTo(n+t)==True:
        print(n+t)
        break
    t+=1