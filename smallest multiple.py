def smallestint(n):
    x=1
    for i in range(2,n+1):
        if x%i!=0:
            for j in range(2,n+1):
                if (x*j)%i==0:
                    x*=j
                    break
    print(x)

smallestint(20)
