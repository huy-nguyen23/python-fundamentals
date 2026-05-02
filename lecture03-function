def isPrime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def sumPrime(n):
    sum=0
    for i in range(1,n):
        if isPrime(i)==True:
           sum+=i
    return sum

n=int(input())
a=sumPrime(n)
print(a)