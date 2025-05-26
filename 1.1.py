def zhegalkin(n, f):
    letters = "abcdefghijklmnopqrstuvwxyz"
    N = 1 << n
    C = f.copy()
    for k in range(1, N):
        for i in range(N-1, k-1, -1):
            C[i] ^= C[i-1]
    monoms = []
    for i, coef in enumerate(C):
        if coef == 0:
            continue
        if i == 0:
            monoms.append("1")
        else:
            bits = []
            for j in range(n):
                if (i >> j) & 1:
                    bits.append(letters[j])
            monoms.append("".join(bits))
    return monoms


if __name__ == "__main__":
    n = int(input())
    f = []
    for _ in range(2 ** n):
        line = [int(i) for i in input().split()]
        f.append(line[-1])
    monoms = zhegalkin(n, f)
    if not monoms:
        print("0")
    else:
        print(" + ".join(monoms))
