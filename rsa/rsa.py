import sys
import math
import random

# Rabin-Miller Algorithm, k is the number of witness
def prime_test(n, k = 100):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n&1 == 0: # the same as n%2 but faster
        return False
    else:
        s, t = 0, n-1
        while t&1 == 0:
            s, t = s+1, t>>1
        # randomly choose witness
        for a in random.sample(xrange(2,min(n-2,sys.maxint)),min(n-4,k)):
            x = pow(a, t, n)
            if x!=1 and x+1!=n:
                for r in xrange(1,s):
                    x = pow(x,2,n)
                    if x == 1:
                        return False
                    elif x == n-1:
                        a = 0
                        break
                if a:
                    return False
        return True

n = random.randint(10**128,10**129)
while not prime_test(n,100):
    n = random.randint(10**128,10**129)
print n
