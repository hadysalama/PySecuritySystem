import binascii
#import StringIO

from decrypt import decrypt
from encrypt import encrypt
from RSA import RSACipher



"""
IMAGINE:
    You have an item and a forged carbon copy you want to securely give to someone.
    You put that item into a lockbox and you lock it with a key and hold onto the carbon copy.
    You then lock that key into a box that you can only be opened with an imprint of the recipient's hand.
    You then toss both boxes into a known location in the ocean and give the carbon copy to the recipient.
    You then tell the recipient to go to the location, salvage the boxes and use his hand to open them.
    Once he takes out he verifies its the same as the carbon copy so he knows he got the right item.
    He is the only person out of 7.5 billion people that can ever open that box even if it gets displaced.
    The item (information) will never be recovered if it gets destroyed.
    This is exactly what's happening here.

Proof of Concept of Adrian Ho's reply on
https://www.quora.com/What-is-the-difference-between-SHA-256-AES-256-and-RSA-2048-bit-encryptions

Done:
    - Tested AES256 with input password
    - Got encryption working
    - Fixed private key error. Flipped params
    - Got entire system working with dict
    - Added try except statements on every decryption function
    - Implement RSA Public/Private Key Generation function
    - Export classes as packages
    - Make a file for encrypt and make a file for decrypt.
    - base64 encode/decode sha256 signatures
    - File Writing
    - Compression/Decompression
    - File Reading.

To Do:
    - Encrypt AES iv and salt values
    - Add suport for any file.
    - Find better AES key than os.urandom.
    - Run test over internet by encrypting a unique file
        I have with Jack's public key and send him only
        the encrypted file, RSA encrypted AES Key, sha256
        signature, and a .pyc or executable of my decryption
        function. Never look at his private key. Don't let him
        edit any code. Don't show him any of the files beforehand.
        Make sure to post to somewhere public. Maybe also have someone
        else try and unlock it.
"""


def main():

    file = open('assets/HappyDance.gif', 'rb')

    binary_data = file.read()

    print('Input is ' + str(len(binary_data)/1000) + ' KB')

    #RSACipher.create_RSA_2048_key_pair()

    (public_key, private_key) = RSACipher.import_keys()

    encrypt(binary_data, public_key)

    file.close()

    compressed_encrypted_dict = open('assets/compressed_encrypted_message.lzma', 'rb')
    encrypted_AES_key = open('assets/encrypted_AES_key.pem', 'rb')
    sha256_signature = open('assets/sha256_signature.txt', 'rb')

    par1 = compressed_encrypted_dict.read()
    par2 = encrypted_AES_key.read()
    par3 = sha256_signature.read()
    

    file = decrypt(par1, par2, par3, private_key)

    compressed_encrypted_dict.close()
    encrypted_AES_key.close()
    sha256_signature.close()

    print('Output is ' + str(len(file)/1000)  + ' KB')

    decrypted_file = open('assets/decrypt.gif','wb')
    bytes = binascii.unhexlify((file.decode()).rstrip('\r\n'))
    decrypted_file.write(bytes) #.decode('utf-8'))
    decrypted_file.close()


if __name__ == '__main__':
    main()


