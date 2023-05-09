
def f(s: int) -> int:
    if s <= 20:
        return 1
    else:
        return f(s - 5) + 5 + s


if __name__ == '__main__':
    s = input()

    print(f(int(s)))
