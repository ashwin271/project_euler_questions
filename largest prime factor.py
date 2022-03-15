def primenumber(n):
    op=True
    l=int(n**0.50)+1
    for i in range (2,l):
        if n%i==0:
            op=False
            break
    return op

def factors(x):
    fct=[]
    for i in range (1,int(x**0.50)+1):
        if x%i==0:
            fct.append(i)
            fct.append(int(x/i))
    return fct

def larprifac(y) :
    f=factors(y)
    lpf=0
    for j in f:
        if primenumber(j):
            if j>lpf:
                lpf=j
    print(lpf)
    
larprifac(600851475143)
    
