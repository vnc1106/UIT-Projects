from requests import *
from Crypto.Cipher import AES
import hashlib


url = "http://aes.cryptohack.org/passwords_as_keys/"

with open("words.txt", 'r') as f:
    words = [w.strip() for w in f.readlines()]

encrypted_flag = get(f"{url}/encrypt_flag").json()['ciphertext']

for keyword in words:
    KEY = hashlib.md5(keyword.encode()).digest()
    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        flag = cipher.decrypt(bytes.fromhex(encrypted_flag))
        if flag.startswith(b'crypto{'):
            print(flag)
            exit()
    except:
        pass

# Flag: crypto{k3y5__r__n07__p455w0rdz?}
        
