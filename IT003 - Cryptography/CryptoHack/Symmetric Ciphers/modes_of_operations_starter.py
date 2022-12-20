from requests import *

url = "http://aes.cryptohack.org/block_cipher_starter/"

s = get(f"{url}/encrypt_flag/").json()

encrypted = s['ciphertext']

s = get(f"{url}/decrypt/{encrypted}").json()

flag = bytes.fromhex(s['plaintext'])

print(flag)

# Flag: crypto{bl0ck_c1ph3r5_4r3_f457_!}