def xor_key(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

k1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
k2_xor_k3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
k1_xor_k2_xor_k3_xor_flag = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

flag = xor_key(k1, xor_key(k2_xor_k3, k1_xor_k2_xor_k3_xor_flag))

print(flag)

# crypto{x0r_i5_ass0c1at1v3}
