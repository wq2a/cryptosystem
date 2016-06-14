# 3 substitution ciphers
M = [-3,['D', 'K', 'V', 'Q', 'F', 'I', 'B', \
      'J', 'W', 'P', 'E', 'S', 'C', 'X', \
      'H', 'T', 'M', 'Y', 'A', 'U', 'O', \
      'L', 'R', 'G', 'Z', 'N'],5]

def encrypt():
    index = 0
    ciphertext = ''
    plaintext = open('symmetric/plaintext.txt','r')
    for line in plaintext:
        for c in line:
            tmp = c
            upper_ascii = ord(c.upper())
            if upper_ascii>=65 and upper_ascii<=90:
                if index == 1:
                    tmp = M[index][upper_ascii-65]
                else:
                    tmp_ascii = upper_ascii+M[index]
                    if tmp_ascii < 65:
                        tmp = chr(tmp_ascii+26)
                    elif tmp_ascii > 90:
                        tmp = chr(tmp_ascii-26)
                    else:
                        tmp = chr(tmp_ascii)
                index += 1
                index %= 3
            ciphertext += tmp
    ct = open('symmetric/ciphertext.txt','w')
    ct.write(ciphertext)
    print 'ciphertext in ciphertext.txt'

def decrypt():
    index = 0
    decrypttext = ''
    ciphertext = open('symmetric/ciphertext.txt','r')
    for line in ciphertext:
        for c in line:
            tmp = c
            upper_ascii = ord(c)
            if upper_ascii>=65 and upper_ascii<=90:
                if index == 1:
                    tmp = chr(M[index].index(c)+65)
                else:
                    tmp_ascii = upper_ascii-M[index]
                    if tmp_ascii < 65:
                        tmp = chr(tmp_ascii+26)
                    elif tmp_ascii > 90:
                        tmp = chr(tmp_ascii-26)
                    else:
                        tmp = chr(tmp_ascii)
                index += 1
                index %= 3
            decrypttext += tmp
    ct = open('symmetric/decrypttext.txt','w')
    ct.write(decrypttext)
    print 'decrpt text in decrypttext.txt'

def main():
    print 'This is Encryption/Decryption using Polyalphabetic Ciphers'
    print 'Ciphertext is in ciphertext.txt and Plaintext is in plaintext.txt.'
    
    command = input('Choose: 1. Encrypt, 2. Decrypt 0. Exit? ')
    while command != 0:
        if command == 1:
            encrypt()
        elif command == 2:
            decrypt()
        else:
            print 'put validate number'
        command = input('Choose: 1. Encrypt, 2. Decrypt 0. Exit? ')

main()
