from Crypto.Cipher import AES
from sys import argv

key = b'Skryptowanie jest super!' # In this MODE, key have to be 24 bytes long
cipher = AES.new(key, AES.MODE_EAX)

# reading file
with open(argv[1], 'rb') as file:
    data = file.read()

nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(data)

print(nonce)
print(ciphertext)
print(tag)

with open(f"{argv[1]}.enc", 'wb') as encfile:
    encfile.write(ciphertext)

with open(f"{argv[1]}.nonce", 'wb') as encfile:
    encfile.write(nonce)

with open(f"{argv[1]}.tag", 'wb') as encfile:
    encfile.write(tag)
