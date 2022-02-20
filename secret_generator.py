import os
import binascii

#Generating a JWT Secret
secret = binascii.hexlify(os.urandom(60))
print(secret)