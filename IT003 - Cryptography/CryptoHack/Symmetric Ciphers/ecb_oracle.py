from requests import *
from string import *
from Crypto.Util.Padding import pad

letter = '{' + '}' + '_' + digits + ascii_lowercase
url = "http://aes.cryptohack.org/ecb_oracle/"

len_flag = 16

for i in range(1,16):
    enc = bytes.fromhex(get(f"{url}/encrypt/{(b'0' * i).hex()}/").json()['ciphertext'])
    if len(enc) > len_flag + 16:
        len_flag += 16 - i
        break

i, j = 0, 8
flag = b''
while len(flag) < len_flag:
    enc = bytes.fromhex(get(f"{url}/encrypt/{(b'0' * j).hex()}/").json()['ciphertext'])
    l = len(enc)
    for char in letter:
        tok = char.encode() + flag
        if len(tok) < 16:
            tok = pad(tok, 16)
        else:
            tok = tok[:16]
        guess = bytes.fromhex(get(f"{url}/encrypt/{(tok).hex()}/").json()['ciphertext'])[:16]
        if guess == enc[l - 16 - i:l - i]:
            flag = char.encode() + flag
            print(f"[+] Found!, flag: {flag}")
            break
    if len(flag)%16 == 15:
        i += 16
    j += 1

print(f"[+] Here's ur flag sir: {flag.decode()}")

# Flag: crypto{p3n6u1n5_h473_3cb}
