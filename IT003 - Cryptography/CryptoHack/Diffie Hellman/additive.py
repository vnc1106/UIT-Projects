from pwn import *
from json import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')


s = remote("socket.cryptohack.org", 13380)

s.recvuntil(b'Intercepted from Alice: ')

alice = loads(s.recvline().decode())

s.recvuntil(b'Intercepted from Bob: ')

bob = loads(s.recvline().decode())

s.recvuntil(b'Intercepted from Alice: ')

enc = loads(s.recvline().decode())

iv, ciphertext = enc['iv'], enc['encrypted']



p, g, A = int(alice['p'], 16), int(alice['g'], 16), int(alice['A'], 16)
B = int(bob['B'], 16)

shared_secret = A * B * pow(g, -1, p) % p

print(decrypt_flag(shared_secret, iv, ciphertext))

# Flag: crypto{cycl1c_6r0up_und3r_4dd1710n?}