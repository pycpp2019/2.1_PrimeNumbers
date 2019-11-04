def primes(n):
    pl = []
    for i in range(2, n):
        pf = True
        si = i**0.5
        for j in pl:
            if j > si + 1:
                break
            if i % j == 0:
                pf = False
                break
        if pf:
            pl.append(i)
    return pl


if __name__ == "__main__":
    with open("prime.txt", "w") as f:
        f.write(" ".join([str(x) for x in primes(10**7)]))
