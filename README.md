# Cryptosystem of RSA and Symmetric Encryption/Decryption
Project 1 is in rsa directory
Project 2 is in symmetric directory

## Project 1
Using RSA method to generate a pair of public and private keys (the minimum length of key is 16 bits)
### Methods
In this project, first of all, the server side will generate two random numbers which differ in the length of several bits to make them more difficult to guess. The key length it specified in the command line is 1024 which means n will have 1024 bit length when key generation is finished. Then it implemented Rabin-Miller Algorithm with 64 witnesses to determin whether those two big number are prime or not. This is a prime probability test, but it would be only 1/(2^128) chance of not being a prime number with 64 witnesses. After that, it randomly generate e and use Euclidean algorithm to check if gcd is 1. Then caculate d.


### Key distribution, encryption and decryption 
Once the key pairs generated, the server side will distribute public key to client side through socket connection. After client side receives the public key, user can choose let server send message to client or let itself send message to server. For example, if choose let server send message, the server first will encrypt the server_plaintext.txt by using its private key and then send the ciphertext to client. Once the client receives the ciphertext, it will decript the message by using server's public key. finnally get the decrypted text. The same as message send from client.

### Use following command to run server
```
make p1
```
If want to change the key size to 16, open the makefile and change 'python rsa/rsa.py 1024' to 'python rsa/rsa.py 16'
The key pairs will be in rsa directory, first line is e or d and the second line is n.

### Use following command to run client
```
make client
```
Choose
#### 1 to send message from server
It will encrypt the message with server's private key and send the cipher to client. The client then decrypts the cipher by using server's public key.

#### 2 to send message from client
It will encrypt the message with server's public key and send the cipher to server. The server then decrypts the cipher by using server's private key.

## Project 2 
Encryption/Decryption using Polyalphabetic Ciphers & Rail Fence

### Use following command
```
make p2
```
Choose
#### 1 to Encrypt (Polyalphabetic)
It will encrypt symmetric/plaintext.txt to symmetric/ciphertext.txt.

#### 2 to Decrypt (Polyalphabetic)
It will decrypt symmetric/ciphertext.txt to symmetric/decrypttext.txt.

#### 3 to Encrypt (Rail Fence)
It will encrypt symmetric/plaintext.txt to symmetric/ciphertext.txt.

#### 4 to Decrypt (Rail Fence)
It will decrypt symmetric/ciphertext.txt to symmetric/decrypttext.txt.

## Other commands
```
make cleanp1
make cleanp2
```
