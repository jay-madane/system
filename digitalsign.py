# pip install cryptography

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat, load_pem_public_key

# Generate a private key
private_key = ec.generate_private_key(ec.SECP256R1())

# Obtain the corresponding public key
public_key = private_key.public_key()

# Message to be signed
message = b"Ayan Sayyad"

# Sign the message
signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))

# Verify the signature
try:
    public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
    print("Signature is valid!")
except Exception:
    print("Signature is invalid.")

# Serialize the public key
serialized_public_key = public_key.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo)

# Deserialize the public key
deserialized_public_key = load_pem_public_key(serialized_public_key)

# Print the serialized public key
print("Serialized Public Key:")
print(serialized_public_key.decode("utf-8"))
