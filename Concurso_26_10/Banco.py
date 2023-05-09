

if __name__ == '__main__':
    import sys
    s = sys.stdin.read().split("\n")

    acciones = int(s[0])
    s.pop(0)

    fila1 = []  # FIFO
    fila2 = []  # LIFO

    for evento in range(acciones):
        eventol = s[evento].split()
        if eventol[0] == 'E':
            if eventol[1] == '1':
                fila1.append(eventol[2])
            else:
                fila2.append(eventol[2])
        if eventol[0] == 'A':
            if eventol[1] == '1':
                print(fila1[0])
                fila1.pop(0)
            else:
                print(fila2[-1])
                fila2.pop()
