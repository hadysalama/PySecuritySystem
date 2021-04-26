import json
import ast

from SHA256 import SHA256
from AES256 import AESCipher
from RSA import RSACipher
from compress import Compressor

"""
Decrypts and verifies message using RSA-2048 Decryption of AES Key, AES Encrypted File, SHA-256 Data Reciept
@author Hady Salama
"""
def decrypt(compressed_encrypted_dict, encrypted_AES_key, sha256_digest, private_key):
    # Attempts to decrypt AES Key using the users RSA2048 private key.
    # If it doesn't work then its the wrong receiver and data is secured.
    #try:
    RSA = RSACipher()
    #encrypted_AES_key = encrypted_AES_key.decode()
    AES_key = RSA.decrypt(private_key, encrypted_AES_key)
    #except ValueError:
    #    message = 'ERROR: Wrong private key. This document was not meant to be decrypted by you.'
    #    return message

    # Makes sure that the data or the key hasn't been corrupted.
    try:
        c = Compressor()
        c.use_lzma()
        encrypted_dict = json.loads(c.decompress(compressed_encrypted_dict))
        encrypted_dict = ast.literal_eval(encrypted_dict)
        AES = AESCipher()
        decrypted = AES.decrypt(encrypted_dict, AES_key)
    except ValueError:
        return 'ERROR: File has been corrupted.'
    except (UnicodeDecodeError, TypeError):
        return 'ERROR: AES256 key has been corrupted.'

    verify = SHA256().verify(decrypted, sha256_digest)


  
    return decrypted

