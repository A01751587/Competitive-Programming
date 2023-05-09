
def rearrange(s: list, concursantes: int) -> list:
    ordenar: list = []
    for orden in range(concursantes):
        st = s[orden].split()
        if st[0] not in ordenar:
            if st[1] == 'null':
                ordenar.insert(0, st[0])
            else:
                ordenar.append(st[0])

        if st[1] not in ordenar:
            if st[1] != 'null':
                index = ordenar.index(st[0])
                ordenar.insert(index, st[1])

    return ordenar


if __name__ == '__main__':
    import sys
    s = sys.stdin.read().split("\n")

    concursantes = int(s[0])
    s.pop(0)

    ans = rearrange(s, concursantes)

    answer = ''
    for person in ans:
        answer += person
        answer += ' '

    print(answer)
