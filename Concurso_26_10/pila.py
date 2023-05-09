

if __name__ == '__main__':
    import sys
    s = sys.stdin.read().split("\n")

    acciones = int(s[0])
    s.pop(0)

    pila = []

    for orden in range(acciones):
        ordenl: list = s[orden].split()
        if ordenl[0] == 'AGREGA':
            pila.append(int(ordenl[1]))
        if ordenl[0] == 'IMPRIME':
            print(pila[-1])
        if ordenl[0] == 'CONSUME':
            if len(pila) >= 2:
                suma = int(pila[-1]) + int(pila[-2])
                pila.pop()
                pila.pop()
                pila.append(suma)
