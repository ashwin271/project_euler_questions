def spepytrip(n):
    op = False
    u=int(n/2)
    for i in range (1,u):
        for j in range (i,u):
            k=((i**2)+(j**2))**0.5
            if k-int(k)==0 :
                if i+j+k==n:
                    print(i*j*k)
                    op=True
                    break
        if op==True:
            break

spepytrip(1000)
