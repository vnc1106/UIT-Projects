from pwn import *
from base64 import b64decode
from Crypto.Util.number import long_to_bytes
import json
from string import ascii_lowercase

def solve(data):
    type = data['type']
    encoded = data['encoded']
    if type == 'bigint':
        return long_to_bytes(int(encoded[2:], 16)).decode()
    if type == 'hex':
        return bytes.fromhex(encoded).decode()
    if type == 'utf-8':
        return bytes(encoded).decode()
    if type == 'base64':
        return b64decode(encoded).decode()
    flag = ""
    for char in encoded:
        if char in ascii_lowercase:
            flag += ascii_lowercase[(ascii_lowercase.index(char) + 13) % 26]
        else:
            flag += "_"
    return flag

s = remote("socket.cryptohack.org", 13377)
for _ in range(100):
    data = json.loads(s.recvline().decode())
    print(data)
    rq = {
        'type':data['type'],
        'decoded':solve(data)
    }

    s.sendline(json.dumps(rq).encode())

print(s.recvline())