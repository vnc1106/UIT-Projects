p = 29
ints = [14, 6, 11]

for a in ints:
    if pow(a, (p - 1)//2, p) == 1:
        for x in range(p):
            if pow(x, 2, p) == a:
                print(f"[+] Flag: {x}")
                exit()

# Flag: 8