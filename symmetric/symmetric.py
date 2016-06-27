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
    print '--- Ciphertext ---'
    print ciphertext
    print '--- Ciphertext has been stored in ciphertext.txt ---'

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
    print '--- Decrpt text ---'
    print decrypttext
    print '--- Decrpt text in decrypttext.txt ---'

def rail_encrypt():
    ciphertext = [[],[],[]]
    cipher = ''
    row = 0
    step = 1
    plaintext = open('symmetric/plaintext.txt','r')
    for line in plaintext:
        for c in line:
            ciphertext[row].append(c)
            if row == 0:
                step = 1
            elif row == 2:
                step = -1
            row += step
    for i in ciphertext:
        for j in i:
            cipher += j
    ct = open('symmetric/rail_ciphertext.txt','w')
    ct.write(cipher)
    print '--- Ciphertext ---'
    print cipher
    print '--- Ciphertext has been stored in rail_ciphertext.txt ---'

def rail_decrypt():
    ciphertext = open('symmetric/rail_ciphertext.txt','r')
    count = 0
    cipher = ''
    for line in ciphertext:
        for c in line:
            cipher += c
            count += 1
    decrypttext = [' ']*count
    row = 0
    init_col = 0
    col = 0
    for c in cipher:
        if col >= count:
            row += 1
            if row > 2:
                break
            init_col += 1
            col = init_col
        decrypttext[col] = c
        if row in [0,2]:
            col += 4
        elif row == 1:
            col += 2
    d = ''
    for i in decrypttext:
        d += i
    ct = open('symmetric/rail_decrypttext.txt','w')
    ct.write(d)
    print '--- Decrpt text ---'
    print d
    print '--- Decrpt text in decrypttext.txt ---'

def main():
    print 'This is Encryption/Decryption using Polyalphabetic Ciphers'
    print 'Ciphertext is in ciphertext.txt and Plaintext is in plaintext.txt.'
    
    command = input('Choose: \
                     \n1. Polyalphabetic encrypt \
                     \n2. Polyalphabetic decrypt \
                     \n3. Rail Fence encrypt \
                     \n4. Rail Fence decrypt \
                     \n0. Exit? ')
    while command != 0:
        if command == 1:
            encrypt()
        elif command == 2:
            decrypt()
        elif command == 3:
            rail_encrypt()
        elif command == 4:
            rail_decrypt()
        else:
            print 'put validate number'
        command = input('Choose: \
                     \n1. Polyalphabetic encrypt \
                     \n2. Polyalphabetic decrypt \
                     \n3. Rail Fence encrypt \
                     \n4. Rail Fence decrypt \
                     \n0. Exit? ')

main()
