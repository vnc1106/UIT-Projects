def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

c = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

known = b'crypto{'

# print(xor(known, c[:7])) => b'myXORke' => guess: key = b'myXORkey'

key, i = "myXORkey", 0

while len(key) < len(c):
    key += key[i]
    i = (i + 1) % len(key)

flag = xor(c, key.encode())

print(flag)

# crypto{0x10_15_my_f4v0ur173_by7e}
