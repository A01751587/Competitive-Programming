

def barbulla(x: int) -> int:
    sumatoria = 0
    for i in range(x + 1):
        if i == 1:
            sumatoria += 1
        else:
            sumatoria += int((i * (i + 1)) / 2)
    return sumatoria


if __name__ == '__main__':
    s = input()

    print(barbulla(int(s)))
