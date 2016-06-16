all:	p1

p1:
	# 1024 is the size of key
	python rsa/rsa.py 1024

p2:
	python symmetric/symmetric.py

showp1:
	cat rsa/PRK
	cat rsa/PUK

cleanp1:
	rm rsa/PRK rsa/PUK

cleanp2:
	rm symmetric/ciphertext.txt symmetric/decrypttext.txt

.PHONY: all p1 p2 clean
