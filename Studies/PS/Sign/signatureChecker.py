from cryptography.hazmat.primitives.asymmetric import ed25519
from sys import argv

## Reading files as bytes

# File to check
with open(argv[1], "rb") as f:
    file_data = f.read()

# Signature
with open(f"{argv[1]}.sig", "rb") as f:
    signature = f.read()

# Public key 
with open(f"{argv[1]}.pub", "rb") as f:
    public_key = f.read()

# Verification
try:
    public_key = ed25519.Ed25519PublicKey.from_public_bytes(public_key)
    public_key.verify(signature, file_data)
    print("File has been verified correctly!")
except Exception:
    print("File has not been verified correctly!")