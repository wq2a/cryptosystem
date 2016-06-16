# Cryptosystem of RSA and Symmetric Encryption/Decryption
Project 1 is in rsa directory
Project 2 is in symmetric directory

## Project 1
Using RSA method to generate a pair of public and private keys (the minimum length of key is 16 bits)
### Methods
In this project, first of all, I generate two random numbers which differ in the length of several bits to make them more difficult to guess. The key length I specified in the command line is 1024 which means n will have 1024 bit length when key generation is finished. Then I implemented Rabin-Miller Algorithm with 64 witnesses to determin whether those two big number are prime or not. This is a prime probability test, but it would be only 1/(2^128) chance of not being a prime number with 64 witnesses. After that, I randomly generate e and use Euclidean algorithm to check if gcd is 1. Then caculate d. 

### Use following command to generate key pairs
```
make p1
```

## Project 2 
Encryption/Decryption using Polyalphabetic Ciphers

### Use following command
```
make p2
```
Choose
#### 1 to Encrypt
It will encrypt symmetric/plaintext.txt to symmetric/ciphertext.txt.

#### 2 to Decrypt
It will decrypt symmetric/ciphertext.txt to symmetric/decrypttext.txt.

## Other commands
```
make cleanp1
make cleanp2
```
