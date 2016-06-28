import rsalib
import socket
import time
def main():
    start = 0
    end = 0
    s = socket.socket()
    host = socket.gethostname()
    port = 5964

    s.connect((host,port))
    key = []
    key.append(int(s.recv(4096))) # e
    s.send('ok')
    key.append(int(s.recv(4096))) # n
    print '--- Public key received ---'
    print key
    
    command = input('Choose:\n1.Receive Message from server\n2.Send Message to server\n0.Exit\n')
    while command != 0:
        if command == 1:
            s.send(str(command))
            cipher = []
            # wait until server is ready
            s.recv(128)
            s.send('ok')
            data = s.recv(4096)
            print '--- Receiving ciphertext from server... ---'
            start = time.time()
            while data != '-1':
                cipher.append(int(data))
                s.send('ok')
                data = s.recv(4096)
            end = time.time()
            print '--- Ciphertext received',end-start,'sec ---'
            print '--- Decrypting ciphertext using Public key... ---'
            start = time.time()
            print rsalib.decrypt('client',cipher,key)
            end = time.time()
            print '--- Done',end-start,'sec ---'
        elif command == 2:
            s.send(str(command))
            # wait until server is ready
            s.recv(128)
            print '--- Encrypting... ---'
            start = time.time()
            cipher = rsalib.encrypt('client',key)
            end = time.time()
            print '--- Ciphertext prepared',end-start,'sec ---'
            print '--- Sending to server... ---'
            start = time.time()
            for i in cipher:
                s.send(str(i))
                # wait until server prepared
                s.recv(128)
            s.send(str(-1))
            end = time.time()
            print '--- Ciphertext sent out',end-start,'sec ---'
        command = input('Choose:\n1.Receive Message from server\n2.Send Message to server\n0.Exit\n')
    s.send(str(0))
    s.close()

main()
