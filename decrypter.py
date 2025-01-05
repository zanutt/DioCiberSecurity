import os
import pyaes

#oppening crypted file
file_name = 'teste.txt.ransowed'
file = open(file_name, 'rb')
file_data = file.read()
file.close()


# Decrypt key
key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
decrypted_data = aes.decrypt(file_data)

#remove encrypted file
os.remove(file_name)

#creating new decrypted file
new_file = 'teste.txt'
open_file = open(f'{new_file}', 'wb')
open_file.write(decrypted_data)
open_file.close()