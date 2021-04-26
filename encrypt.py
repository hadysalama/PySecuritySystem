import os
import json

from SHA256 import SHA256
from AES256 import AESCipher
from RSA import RSACipher
from compress import Compressor

"""
Outputs RSA-2048 Encrypted AES Key, AES Encrypted File, SHA-256 Data Reciept
@author Hady Salama
"""
def encrypt(message, public_key):

    sha256 = SHA256()
    sha256_signature = sha256.create_hash(message)

    random_AES_key = os.urandom(32) # 32 Bytes 256 Bit Key

    AES = AESCipher()
    encrypted = AES.encrypt(message, random_AES_key) #message.decode()

    cipher_message = open('assets/compressed_encrypted_message.lzma','wb')
    c = Compressor()
    c.use_lzma()
    cipher_message.write(c.compress(json.dumps(str(encrypted))))#str(encrypted).encode())
    cipher_message.close()

    RSA = RSACipher()
    encrypted_AES_key = RSA.encrypt(public_key, random_AES_key)
    cipher_AES_key = open('assets/encrypted_AES_key.pem','wb')
    cipher_AES_key.write(encrypted_AES_key)
    cipher_AES_key.close()

    return {
        'sha256_signature': sha256_signature,
        'encrypted_AES_key': encrypted_AES_key,
        'encrypted_file': encrypted['cipher_text'],
        'salt': encrypted['salt'],
        'iv': encrypted['iv']
    }

