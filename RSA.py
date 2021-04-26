import base64

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto import Random

"""
RSA-2048 Encryption and Decryption Utility Class.
@author Hady Salama
"""
class RSACipher(object):
    def __init__(self):
        pass

    def encrypt(self, public_key, raw):
        cipher = PKCS1_OAEP.new(public_key)
        ciphertext = cipher.encrypt(raw)
        return base64.b64encode(ciphertext)

    def decrypt(self, private_key, cipher_text):
        cipher = PKCS1_OAEP.new(private_key)
        message = cipher.decrypt(base64.b64decode(cipher_text))
        return message

    def import_keys():
        try:
            pub = open('assets/pubkey.pem', 'r')
            priv = open('assets/privkey.pem', 'r')
            
            public_key = RSA.importKey(str(pub.read()))
            private_key = RSA.importKey(str(priv.read()))
            
            pub.close()
            priv.close()

            return (public_key, private_key)

        except FileNotFoundError:
            return ('Keys not found. Please place them in current directory.','')

    def create_RSA_2048_key_pair():
        random_generator = Random.new().read
        keys = RSA.generate(2048, random_generator)
        priv = open('assets/privkey.pem','wb')
        priv.write(keys.export_key('PEM'))
        priv.close()

        pub = open('assets/pubkey.pem','wb')
        pub.write(keys.publickey().export_key('PEM'))
        pub.close()
        

