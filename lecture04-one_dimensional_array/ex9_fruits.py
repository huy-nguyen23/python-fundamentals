def fruits():
    n=int(input())
    maxTao=-1
    maxCam=-1
    index=0
    for i in range(n):
            a,b=map(int,input().split())
            if maxTao<a :
                  maxTao=a
                  index=i+1
                  maxCam=b
            elif maxTao==a:
                  if maxCam<b:
                        maxCam=b
                        index=i+1
    return index
a=fruits()
print(a)