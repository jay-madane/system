# pip install pycryptodome

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

# Function to encrypt a message using DES
def des_encrypt(plaintext, key):
    cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    padded_text = pad(plaintext.encode('utf-8'), DES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return binascii.hexlify(encrypted_text).decode('utf-8')

# Function to decrypt a message using DES
def des_decrypt(encrypted_text, key):
    cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    encrypted_text_bytes = binascii.unhexlify(encrypted_text.encode('utf-8'))
    decrypted_text = unpad(cipher.decrypt(encrypted_text_bytes), DES.block_size)
    return decrypted_text.decode('utf-8')

# Get user input for plaintext and key
plaintext = input("Enter the plaintext message: ")
key = input("Enter an 8-byte key: ")

# Ensure the key is 8 bytes long
if len(key) != 8:
    print("Error: The key must be exactly 8 bytes long.")
else:
    # Encrypt the plaintext
    encrypted_text = des_encrypt(plaintext, key)
    print(f"Encrypted message: {encrypted_text}")

    # Decrypt the message
    decrypted_text = des_decrypt(encrypted_text, key)
    print(f"Decrypted message: {decrypted_text}")
