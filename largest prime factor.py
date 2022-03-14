def primenumber(n):
    op=True
    l=int(n**0.50)+1
    for i in range (2,l):
        if n%i==0:
            op=False
            break
    return op

def larprifac(x) :
    factors=[]
    lpf=0
    for i in range (1,int(x**0.50)+1):
        if x%i==0:
            factors.append(i)
            factors.append(int(x/i))
    for j in factors:
        if primenumber(j):
            if j>lpf:
                lpf=j
    print(lpf)
    
larprifac(600851475143)
    
