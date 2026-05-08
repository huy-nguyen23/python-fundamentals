def Pruningflowers():
            n=int(input())
            a=list(map(int,input().split()))
            min=a[0]
            for x in a:
                    if x<min:
                        min=x
            nangluong=0
            for x in a:
                    nangluong+=(x-min)
            return nangluong                 
a=Pruningflowers()
print(a)