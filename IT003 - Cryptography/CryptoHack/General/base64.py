from base64 import b64encode
hex_encoded = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
hex_to_bytes = bytes.fromhex(hex_encoded)
flag = b64encode(hex_to_bytes)

print(flag)

# Flag: crypto/Base+64+Encoding+is+Web+Safe/