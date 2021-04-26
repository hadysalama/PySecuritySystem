import os
import base64
import hashlib

from Crypto.Cipher import AES
from Crypto import Random


"""
AES-256 Encryption and Decryption Utility Class.
@author Lane Wagner
https://medium.com/qvault/aes-256-cipher-python-cryptography-examples-b877b9d2e45e
"""
class AESCipher(object):
    def __init__(self):
        pass

    # pad with spaces at the end of the text
    # beacuse AES needs 16 byte blocks
    def pad(self, s):
        block_size = AES.block_size  # 16
        remainder = len(str(s)) % block_size
        padding_needed = block_size - remainder
        return str(s) + padding_needed * ' '

    # remove the extra spaces at the end
    def unpad(self, s):
        return s.rstrip()

    def encrypt(self, plain_text, password):
        # generate a random salt
        salt = os.urandom(AES.block_size)

        # generate a random iv
        iv = Random.new().read(AES.block_size)

        # use the Scrypt KDF to get a private key from the password
        private_key = hashlib.scrypt(
            password, salt=salt, n=2**14, r=8, p=4, dklen=32)

        # pad text with spaces to be valid for AES CBC mode
        padded_text = self.pad(plain_text)

        # create cipher config
        cipher_config = AES.new(private_key, AES.MODE_CBC, iv)

        # return a dictionary with the encrypted text
        return {
            'cipher_text': base64.b64encode(cipher_config.encrypt(padded_text.encode())),
            'salt': base64.b64encode(salt),
            'iv': base64.b64encode(iv)
        }

    def decrypt(self, enc_dict, password):
        # decode the dictionary entries from base64
        enc = base64.b64decode(enc_dict['cipher_text'])
        salt = base64.b64decode(enc_dict['salt'])
        iv = base64.b64decode(enc_dict['iv'])

        # generate the private key from the password and salt
        private_key = hashlib.scrypt(password, salt=salt, n=2**14, r=8, p=4, dklen=32)

        # create the cipher config
        cipher = AES.new(private_key, AES.MODE_CBC, iv)

        # decrypt the cipher text
        decrypted = cipher.decrypt(enc)

        # unpad the text to remove the added spaces
        original = self.unpad(decrypted)

        return original
