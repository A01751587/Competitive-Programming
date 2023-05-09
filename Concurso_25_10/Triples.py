def printer(pos: list) -> str:
    res = ''
    for num in pos:
        res += str(num)
        res += ' '
    return res


def check_triples(s: list):
    count = 0
    pos: list = []
    for num in range(1, s[0] + 1):
        if s[num] % 3 == 0:
            count += 1
            pos.append(num)
    if count == 0:
        return "No hay triples."
    else:
        print(count)
        return printer(pos)


if __name__ == '__main__':
    import sys
    s = [int(x) for x in sys.stdin.read().split()]

    print(check_triples(s))
