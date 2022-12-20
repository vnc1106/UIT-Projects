def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

c = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

known = b'crypto{'

# print(xor(known, c[:7])) => b'\x10\x10\x10\x10\x10\x10\x10' => key = b'\x10'

key = b'\x10'

flag = xor(c, key * len(c))

print(flag)

# crypto{0x10_15_my_f4v0ur173_by7e}
