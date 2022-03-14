import time
start_time = time.time()

def palindrome(n):
    if str(n)==str(n)[-1::-1]:
        return True
    else:
        return False
def highestprod(n):
    global x
    x=''
    for i in range (n):
        x+='9'
    x=int(x)
    return x**2

def smallestprod(n):
    global y
    y=''
    for i in range (n):
        y+='1'
    y=int(y)
    return y**2

def lpp(n):
    lst=[]
    k=highestprod(n)
    l=smallestprod(n)
    for i in range(k,int(k/1.15),-1):
        if i%10==0:
            pass
        elif palindrome(i):
            lst.append(i)
    val=0
    for m in lst:
        no=int(x)
        while True:
            if no<y:
                break
            elif m%no==0 and x>(m/no)>y and no>y:
                val=m
                break
            else:
                no-=1
        if val:
            break
    print(val)

lpp(3) #<<<==== type here

print("--- %s seconds ---" % (time.time() - start_time))
