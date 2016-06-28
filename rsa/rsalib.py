import sys
import math
import random

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
    prime = random.randint(2**(length),2**(length+1))
    while not prime_test(prime,64):
        prime = random.randint(2**(length),2**(length+1))
    return prime

# Euclidean algorithm
def gcd(a, b):
    while b != 0:
        t = b
        b = a%b
        a = t
    return a

# find d that (ed mod totient) = 1
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

# break down x (the exponent) into power of 2
def int2BaseTwo(x):
    bitInverse = []
    while x != 0:
        bitInverse.append(x & 1)
        x >>= 1
    return bitInverse

# Modular Exponentiation
def modular_exponentiation(m,d,n):
    base2D = int2BaseTwo(d)
    length = len(base2D)
    modArr = []
    result = 1
    for i in range(1, length+1):
        if i == 1:
            modArr.append(m % n)
        else:
            modArr.append((modArr[i-2]**2)%n)
    for i in range(0, length):
        if base2D[i] == 1:
            result *= base2D[i]*modArr[i]
    return result % n

# encryption key[0] is d, key[1] is n
def encrypt(hosttype, key):
    cipher_dic = {}
    ciphertext = []
    plaintext = open('rsa/'+hosttype+'_plaintext.txt','r')
    for line in plaintext:
        for c in line:
            c_ascii = ord(c)
            c_cipher = 0
            if c_ascii in cipher_dic.keys():
                c_cipher = cipher_dic[c_ascii]
            else:
                c_cipher = modular_exponentiation(c_ascii,key[0],key[1])
                cipher_dic[c_ascii] = c_cipher
            ciphertext.append(c_cipher)
    ct = open('rsa/'+hosttype+'_ciphertext.txt','w')
    for i in ciphertext:
        ct.write(str(i)+'\n')
    ct.close()
    return ciphertext

# decryption key[0] is e, key[1] is n
def decrypt(fn, ciphertext, key):
    decrypt_dic = {}
    decrypttext = ''
    if len(ciphertext) == 0:
        ciphertext = open('rsa/'+hosttype+'_ciphertext.txt','r')
    for c_cipher in ciphertext:
        c_decrypt = ''
        if c_cipher in decrypt_dic.keys():
            c_decrypt = decrypt_dic[c_cipher]
        else:
            c_decrypt = modular_exponentiation(int(c_cipher),key[0],key[1])
            decrypt_dic[c_cipher] = c_decrypt
        decrypttext += chr(c_decrypt)
    return decrypttext
