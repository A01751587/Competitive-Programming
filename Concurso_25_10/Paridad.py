
def check_parity(n: str) -> str:
    count = 0
    for char in n:
        if char == "1":
            count += 1
    if count % 2 == 0:
        res = n + "0"
    else:
        res = n + "1"
    return res


if __name__ == '__main__':
    s = input()

    print(check_parity(s))
