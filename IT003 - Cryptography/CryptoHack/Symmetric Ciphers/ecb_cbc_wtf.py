from requests import *
from pwn import xor

url = "http://aes.cryptohack.org/ecbcbcwtf/"
s = bytes.fromhex(get(f"{url}/encrypt_flag").json()['ciphertext'])

iv, encrypted_block = s[:16], [s[k : k + 16] for k in range(16, len(s), 16)]

flag = b''

for block in encrypted_block:
    s = get(f"{url}/decrypt/{block.hex()}/").json()['plaintext']
    flag += xor(bytes.fromhex(s), iv)

    iv = block

print(flag)

# Flag: crypto{3cb_5uck5_4v01d_17_!!!!!}