import sys

if __name__ == '__main__':

    s = (int(x) for x in sys.stdin.read().split())

    procesos = next(s)
    tiempo = next(s)

    listaprocesos = []
    listatiempos = []

    for i in range(procesos):
        llave = next(s)
        valor = next(s)
        division = valor // tiempo
        if valor % tiempo != 0:
            listaprocesos.append(llave)
            listatiempos.append(division + 1)
        else:
            listaprocesos.append(llave)
            listatiempos.append(division)

    for indice in range(len(listatiempos)):
        minimo = min(listatiempos)
        indicearemover = listatiempos.index(minimo)
        print(listaprocesos[indicearemover])
        listaprocesos.pop(indicearemover)
        listatiempos.pop(indicearemover)
