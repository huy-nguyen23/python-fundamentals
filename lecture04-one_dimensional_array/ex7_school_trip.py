def schooltrip():
      n=int(input())
      a=list(map(int,input().split()))
      countNam=0
      countNu=0
      for x in a:
            if x==0:
                  countNam+=1
            elif x==1:
                  countNu+=1
      if countNu==countNam:
            print('YES')
      else:
            print('NO')
      return
schooltrip()