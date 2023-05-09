def check_prom(proms: list) -> int:
    suma = 0
    for n in proms:
        suma += n
    return suma // 5


if __name__ == '__main__':
    import sys
    s = sys.stdin.read().split("\n")
    hijos = int(s[0])

    for prom in range(1, hijos + 1):
        proms: list = [int(x) for x in s[prom].split()]
        promedio_hijo = check_prom(proms[:-1])
        if promedio_hijo != proms[-1]:
            print(prom, promedio_hijo)
