from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from pathlib import Path
import datetime
import time

key = RSA.generate(2048)
private_key = key.export_key('PEM')
public_key = key.publickey().exportKey('PEM')
message = Path (input("Please enter your file location: ")).read_text()
#---------timestamp Start-------------
start_time = time.perf_counter_ns()
#---------Encryption------------------
message = str.encode(message)

rsa_public_key = RSA.importKey(public_key)
rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
encrypted_text = rsa_public_key.encrypt(message)
#---------timestamp Stop-------------
end_time = time.perf_counter_ns()
print('Execution Time in Nanoseconds :', end_time - start_time)
#-------------------------------------
#---------output file-----------------
with open(input("Please enter your Encrypted file name: "), 'w') as f:
    f.write(format(encrypted_text))
print("Generating encrypted file ")
print('')
#-----------End of Encryption---------

#-------------Decryption-------------=
print("Starting Decryption ")
rsa_private_key = RSA.importKey(private_key)
rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
#---------timestamp Start-------------
start_time = time.perf_counter_ns()
decrypted_text = rsa_private_key.decrypt(encrypted_text)
#---------timestamp Stop-------------
end_time = time.perf_counter_ns()
print('Execution Time in Nanoseconds :', end_time - start_time)
#-------------------------------------
#---------output file-----------------
with open(input("Please enter your Decrypted file name: "), 'w') as f:
    f.write(format(decrypted_text))
print("Generating Decrypted file ")
