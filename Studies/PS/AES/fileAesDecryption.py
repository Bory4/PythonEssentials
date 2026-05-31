from Crypto.Cipher import AES
from sys import argv

key = b'Skryptowanie jest super!'# In this MODE, key have to be 16 bytes long

with open(f"{argv[1]}.enc", 'rb') as data:
    ciphertext = data.read()

with open(f"{argv[1]}.nonce", 'rb') as data:
    nonce=data.read()

with open(f"{argv[1]}.tag", 'rb') as data:
    tag=data.read()

cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)

try:
    cipher.verify(tag)
    with open(f"{argv[1]}.dec", "wb") as file:
        file.write(plaintext)
except ValueError:
    print("Key incorrect or message corrupted")

