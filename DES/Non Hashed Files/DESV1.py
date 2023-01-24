from Crypto.Cipher import DES
import binascii
from pathlib import Path
import datetime
import time

key = input('Enter your key: ').encode('utf-8')
myDes = DES.new(key, DES.MODE_ECB)
print('Please select option:\n1. Encryption\n2. Decryption\n3. Exit')

while True:
    user_choice = input("Choose a option: ")
    if user_choice == "1":
        #input file
        plain_text = Path (input("Please enter your file location: ")).read_text()
        #---------timestamp Start-------------
        start_time = time.perf_counter_ns()
        cipher_text = myDes.encrypt(plain_text.encode("utf-8"))
        end_time = time.perf_counter_ns()
        print('Execution Time in Nanoseconds :', end_time - start_time)
        print('')
        #---------timestamp Stop-------------
        #output file
        with open(input("Please enter your file name: "), 'w') as f:
            f.write(cipher_text.hex())
        print("Generating encrypted file ")
        #print("Encrypted text:", cipher_text.hex())

    elif user_choice == "2":
        user_cipher_text = Path (input("Please enter your file location: ")).read_text()
        #---------timestamp Start-------------
        start_time = time.perf_counter_ns()
        text = myDes.decrypt(binascii.unhexlify(user_cipher_text))
        end_time = time.perf_counter_ns()
        print('Execution Time in Nanoseconds :', end_time - start_time)
        print('')
        #---------timestamp Stop-------------
        with open(input("Please enter your file name: "), 'w') as f:
            f.write(text.decode('utf-8'))
        print("Generating decrypted file ")
        #print("Decrypted text:", text.decode('utf-8'))

    elif user_choice == "3":
        print("Quitting The Program....")
        break
    else:
        print("Please Choose a correct option")
