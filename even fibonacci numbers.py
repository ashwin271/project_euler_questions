a,b,s=1,1,0
while True:
    a,b=b,a+b
    if a>4000000:
        break
    if a%2==0:
        s+=a

print(s)
