def main():
    n, m = map(int, input().split())
    
    A = [[False] * m for _ in range(m)]
    
    for _ in range(n):
        u, v = map(int, input().split())
        A[u-1][v-1] = True

    reflexive = all(A[i][i] for i in range(m))

    transitive = True
    for i in range(m):
        for j in range(m):
            if A[i][j]:
                for k in range(m):
                    if A[j][k] and not A[i][k]:
                        transitive = False
                        break
                if not transitive:
                    break
        if not transitive:
            break

    antisymm = True
    for i in range(m):
        for j in range(m):
            if i != j and A[i][j] and A[j][i]:
                antisymm = False
                break
        if not antisymm:
            break

    print("Рефлексивное" if reflexive else "Антирефлексивное")
    print("Транзитивное" if transitive else "Нетранзитивное")
    print("Антисимметричное" if antisymm else "Неантисимметричное")


if __name__ == "__main__":
    main()
