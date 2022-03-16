def ssd(n):
    s1=0
    s2=0
    for i in range(1,n+1):
        s1+=i
        s2+=i**2
    s1**=2
    print(s1-s2)

ssd(100)
