import hashlib
import base64

"""
Creates SHA256 Hash Signature and verifies messages against previously created signatures.
@author Hady Salama
"""


class SHA256(object):
    def __init__(self):
        self.debug_val = ''

    def debug(self, val):
        self.debug_val = val
        #print(val)
        return self.debug_val

    def create_hash(self, message):
        self.debug(hashlib.sha256(message).digest())
        hash = base64.b64encode(hashlib.sha256(message).digest()) #.encode()
        signature = open('assets/sha256_signature.txt','wb')
        signature.write(hash)
        signature.close()
        return hash

    def verify(self, message, hash):
        #print(hash)
        hash = base64.b64decode(hash)
        #print(hash)
        #print(self.debug_val)
        #debug_bool = self.debug_val == hashlib.sha256(message.encode()).digest()
        #print('DEBUG: ' + str(debug_bool))
        return hash == hashlib.sha256(message).digest()

