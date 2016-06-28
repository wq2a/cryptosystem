all:	p1

p1:
	# 1024 is the size of key
	python rsa/rsa.py 1024

client:
	python rsa/client.py

p2:
	python symmetric/symmetric.py

showp1:
	cat rsa/PRK
	cat rsa/PUK

cleanp1:
	rm rsa/PRK rsa/PUK rsa/rsalib.pyc rsa/server_ciphertext.txt rsa/client_ciphertext.txt

cleanp2:
	rm symmetric/ciphertext.txt symmetric/decrypttext.txt symmetric/rail_ciphertext.txt symmetric/rail_decrypttext.txt

.PHONY: all p1 client p2 clean
