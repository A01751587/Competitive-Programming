def numeroypico(n: int) -> int:
    if n == 1:
        return n
    else:
        return n + numeroypico(n // 2)


if __name__ == '__main__':
    s = input()

    print(numeroypico(int(s)))
