def prime(n):
    l=int(n**0.50)+1
    for i in range (2,l):
        if n%i==0:
            return False
    else:
        return True

def nth_prime(n):
    p=0
    x=2
    while True :
        if prime(x):
            p+=1
        if p==n:
            print(x)
            break
        x+=1

nth_prime(10001)
