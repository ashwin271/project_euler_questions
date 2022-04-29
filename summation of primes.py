#function to check if a number is prime or not

def prime(n):
    l=int(n**0.50)+1
    for i in range (2,l):
        if n%i==0:
            return False
    else:
        return True

#function to return the sum of prime numbers from 1 to 'n'
def prime_sum(n):
    sum = 0
    for i in range(2,n):
        if prime(i):
            sum+=i
    print(sum)

prime_sum(2000000)
