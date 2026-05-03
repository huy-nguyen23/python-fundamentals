def gcd(a,b): 
    while b!=0:
        a,b=b,a%b
    return a
a,b=map(int,input().split())
x=gcd(a,b)
c=a//x
d=b//x
print(f'{c} {d}')