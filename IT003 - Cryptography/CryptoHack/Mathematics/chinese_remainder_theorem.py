from gmpy2 import gcd

def crt(a, m):
    M, D, n = 1, 0, len(m)
    for x in m:
        M, D = M*x, gcd(D, x)
    if D != 1:
        return -1
    b = [M//x for x in m]
    c = [pow(b[i], -1, m[i]) for i in range(n)]
    x = 0
    for i in range(n):
        x = (x + a[i]*b[i]*c[i])%M
    return x

a = [2, 3, 5]
m = [5, 11, 17]

x = crt(a, m)

print(f"Flag: {x}")

# Flag: 872