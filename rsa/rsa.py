import sys
import math
import random
import base64

# Rabin-Miller Algorithm, k(64) is the number of witness 1/(2**128) chance of not being prime
def prime_test(n, k = 64):
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
        # randomly choose witnesses
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

def generate_prime(length):
    prime = random.randint(10**(length),10**(length+1))
    while not prime_test(prime,64):
        prime = random.randint(10**(length),10**(length+1))
    return prime

# Euclidean algorithm
def gcd(a, b):
    while b != 0:
        t = b
        b = a%b
        a = t
    return a

def modular_multiplicative_inverse(a,n):
    t, nt = 0, 1
    r = n
    nr = a%n
    if n < 0:
        n = -n
    if a < 0:
        a = n-(-a%n)
    while nr != 0:
        quot = (r/nr)|0
        tmp = nt
        nt = t-quot*nt
        t = tmp
        tmp = nr
        nr = r-quot*nr
        r = tmp
    if r > 1:
        return -1
    if t < 0:
        t += n
    return t 

def main():
    if len(sys.argv) < 2:
        print 'Need the length of key'
        return
    mid = int(sys.argv[1])//2
    p = generate_prime(mid-5)
    q = generate_prime(mid+5)
    n = p*q
    t = (p-1)*(q-1) # totient

    e = random.randint(1,t)
    while gcd(t,e) != 1:
        e = random.randint(1,t)

    #print e
    d = modular_multiplicative_inverse(e,t)
    pub = open('pub.pem','w')
    # pub.write('----BEGIN RSA PUBLIC KEY----\n')
    pub.write(base64.b64encode(str(n)+str(e))+'\n')
    # pub.write('----END RSA PUBLIC KEY----')
    pri = open('pri.pem','w')
    # pri.write('----BEGIN RSA PRIVATE KEY----\n')
    pri.write(base64.b64encode(str(n)+str(d))+'\n')
    # pri.write('----END RSA PRIVATE KEY----')
    print d

main()
