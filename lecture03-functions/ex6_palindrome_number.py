def soDoiXung(n):
      bienLuuTru=0
      while n>0:
             chuSo=n%10
             bienLuuTru=bienLuuTru*10+chuSo
             n//=10
      return bienLuuTru
n=int(input())
a=soDoiXung(n)
if n==a:
       print('YES')
else:
       print('NO')