g, p = 2, 28151

while True:
    tmp = [pow(g, x, p) for x in range(2, p - 1) if (p - 1)%x == 0]
    if 1 not in tmp:
        print(f"[+] Smallest primitive root: {g}")
        exit()
    g += 1

# [+] Smallest primitive root: 7
