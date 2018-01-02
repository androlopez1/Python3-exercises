import math

def isPrime(n):
    if math.factorial(n-1)% n == 0:
        print ('Not prime')
    else:
        print('Prime')
    
p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    isPrime(n)
    
