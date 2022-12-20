N = 0xb8af3d3afb893a602de4afe2a29d7615075d1e570f8bad8ebbe9b5b9076594cf06b6e7b30905b6420e950043380ea746f0a14dae34469aa723e946e484a58bcd92d1039105871ffd63ffe64534b7d7f8d84b4a569723f7a833e6daf5e182d658655f739a4e37bd9f4a44aff6ca0255cda5313c3048f56eed5b21dc8d88bf5a8f8379eac83d8523e484fa6ae8dbcb239e65d3777829a6903d779cd2498b255fcf275e5f49471f35992435ee7cade98c8e82a8beb5ce1749349caa16759afc4e799edb12d299374d748a9e3c82e1cc983cdf9daec0a2739dadcc0982c1e7e492139cbff18c5d44529407edfd8e75743d2f51ce2b58573fea6fbd4fe25154b9964d
e = 0x9ab58dbc8049b574c361573955f08ea69f97ecf37400f9626d8f5ac55ca087165ce5e1f459ef6fa5f158cc8e75cb400a7473e89dd38922ead221b33bc33d6d716fb0e4e127b0fc18a197daf856a7062b49fba7a86e3a138956af04f481b7a7d481994aeebc2672e500f3f6d8c581268c2cfad4845158f79c2ef28f242f4fa8f6e573b8723a752d96169c9d885ada59cdeb6dbe932de86a019a7e8fc8aeb07748cfb272bd36d94fe83351252187c2e0bc58bb7a0a0af154b63397e6c68af4314601e29b07caed301b6831cf34caa579eb42a8c8bf69898d04b495174b5d7de0f20cf2b8fc55ed35c6ad157d3e7009f16d6b61786ee40583850e67af13e9d25be3
c = 0x3f984ff5244f1836ed69361f29905ca1ae6b3dcf249133c398d7762f5e277919174694293989144c9d25e940d2f66058b2289c75d1b8d0729f9a7c4564404a5fd4313675f85f31b47156068878e236c5635156b0fa21e24346c2041ae42423078577a1413f41375a4d49296ab17910ae214b45155c4570f95ca874ccae9fa80433a1ab453cbb28d780c2f1f4dc7071c93aff3924d76c5b4068a0371dff82531313f281a8acadaa2bd5078d3ddcefcb981f37ff9b8b14c7d9bf1accffe7857160982a2c7d9ee01d3e82265eec9c7401ecc7f02581fd0d912684f42d1b71df87a1ca51515aab4e58fab4da96e154ea6cdfb573a71d81b2ea4a080a1066e1bc3474

from gmpy2 import iroot
from Crypto.Util.number import *

def wiener_attack(e, N):
    frlst = []
    def expand_fraction_list_gen(a, b):
        n, r = a//b, a%b
        frlst.append(n)
        if r == 0:
            return 
        expand_fraction_list_gen(b, r)
    expand_fraction_list_gen(e, N)
    def cal(i):
        k_pre, d_pre = 0, 1
        while i >= 0:
            k_cur = d_pre
            d_cur = frlst[i]*d_pre + k_pre
            k_pre, d_pre = k_cur, d_cur
            i -= 1
        return d_cur, k_cur
    def quadratic(a, b, c):
        delta = b**2 - 4*a*c
        if delta < 0:
            return -1
        else:
            sqr, t = iroot(delta, 2)
            if t:
                return (-b + sqr)//(2*a)
            else:
                return -1
    for i in range(1, len(frlst)):
        k, d = cal(i)
        s = N + 1 - (e*d - 1)//k
        p = quadratic(1, -s, N)
        if p > 0 and N%p == 0:
            break
    return long_to_bytes(pow(c, d, N))

print(wiener_attack(e, N))

# crypto{s0m3th1ng5_c4n_b3_t00_b1g}
