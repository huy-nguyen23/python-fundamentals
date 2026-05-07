def soLike():
      n=int(input())
      a=list(map(int,input().split()))
      for x in a:
            if x==0:
                  print('NO')
                  return
      print('YES')
soLike()