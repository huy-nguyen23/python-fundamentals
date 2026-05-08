def soNguyenTo(n):    
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
def demSoNguyenTo():
      n=int(input())
      a=list(map(int,input().split()))
      count=0
      for x in a:
          if soNguyenTo(x)==True:
              count+=1
      return count
a=demSoNguyenTo()
print(a)