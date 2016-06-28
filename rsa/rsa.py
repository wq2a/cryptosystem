import sys
import math
import random
import socket
import time
import rsalib

def main():
    if len(sys.argv) < 2:
        print 'Need the length of key'
        return
    # timer
    start = 0
    end = 0
    print '--- Generating key pairs ---'
    start = time.time()
    mid = int(sys.argv[1])//2
    p = rsalib.generate_prime(mid-5)
    print '--- prime p ---\n',p
    q = rsalib.generate_prime(mid+5)
    print '--- prime q ---\n',q
    n = p*q
    print '--- n ---\n',n
    t = (p-1)*(q-1) # totient
    print '--- totient ---\n',t
    e = random.randint(1,t)
    while rsalib.gcd(t,e) != 1:
        e = random.randint(1,t)
    print '--- e ---\n',e
    d = rsalib.modular_multiplicative_inverse(e,t)
    print '--- d ---\n',d

    puk = open('rsa/PUK','w')
    puk.write(str(e)+'\n')
    puk.write(str(n))
    puk.close()
    prk = open('rsa/PRK','w')
    prk.write(str(d)+'\n')
    prk.write(str(n))
    prk.close()
    end = time.time()

    key = [d,n]
    print '--- Key pairs have been generated. ',end-start,'sec ---'
    
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = socket.gethostname()
    port = 5964
    s.bind((host, port))
    s.listen(5)
    print '--- Wait for client connection ---'
    c, addr = s.accept()
    print '--- Got connection from ', addr,' ---'
    print '--- Distribute public key ---'
    start = time.time()
    c.send(str(e))
    # wait until client received, and send back ack 'ok'
    c.recv(128)
    c.send(str(n))
    end = time.time()
    print '--- Key distribution done.',end-start,'sec ---'
    command = c.recv(128)
    while command != '0':
        print '--- Command from client:',command
        if command == '1':
            print '--- Encrypting... ---'
            start = time.time()
            c.send('ok')
            c.recv(128)
            cipher = rsalib.encrypt('server',key)
            end = time.time()
            print '--- Ciphertext prepared',end-start,'sec ---'
            # print cipher
            print '--- Sending to client... ---'
            start = time.time()
            for i in cipher:
                c.send(str(i))
                # wait until client prepared
                c.recv(128)
            end = time.time()
            print '--- Ciphertext sent out',end-start,'sec ---'
            c.send(str(-1))
        elif command == '2':
            cipher_client = []
            c.send('ok')
            data = c.recv(4096)
            print '--- Receiving ciphertext from client... ---'
            start = time.time()
            while data != '-1':
                cipher_client.append(int(data))
                c.send('ok')
                data = c.recv(4096)
            end = time.time()
            print '--- Ciphertext received',end-start,'sec ---'
            print '--- Decrypting ciphertext using Private key... ---'
            start = time.time()
            print rsalib.decrypt('server',cipher_client,key)
            end = time.time()
            print '--- Done',end-start,'sec ---'
            #print cipher_client
        # c.recv(128)
        command = c.recv(128)
    c.close()
    s.close()

    print '--- Connection closed ---'






    # key = [d,n]
    # encrypt(key)
    # key = [e,n]
    # decrypt(key)

    # print int2BaseTwo(127)
    # cc = modular_exponentiation(127,d,n)
    # print cc
    # print modular_exponentiation(cc,e,n)
    # pub.write('----BEGIN RSA PUBLIC KEY----\n')
    # pub.write(base64.b64encode(str(n)+str(e))+'\n')
    # pub.write('----END RSA PUBLIC KEY----')
    # pri = open('pri.pem','w')
    # pri.write('----BEGIN RSA PRIVATE KEY----\n')
    # pri.write(base64.b64encode(str(n)+str(d))+'\n')
    # pri.write('----END RSA PRIVATE KEY----')

main()
