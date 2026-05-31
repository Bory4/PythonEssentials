from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization
from sys import argv

# Generating pair of keys
private_key = ed25519.Ed25519PrivateKey.generate()
public_key = private_key.public_key()

public_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PublicFormat.Raw
)

# Checking input parameters
if len(argv) != 2:
    print(f"Usage: python {argv[0]} <path_to_file>")
    exit(1)

# Reading file as bytes
with open(argv[1], "rb") as f:
    file_data = f.read()

# Signing file using private key
signature = private_key.sign(file_data)

# Saving signature as bytes
with open(f"{argv[1]}.sig", "wb") as f:
    f.write(signature)

# Saving public key as bytes
with open(f"{argv[1]}.pub", "wb") as f:
    f.write(public_bytes)

print("Signed!")
print(f"Public key in hex: {public_bytes.hex()}")
print(f"Sign in hex: {signature.hex()}") 