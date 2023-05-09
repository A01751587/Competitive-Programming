import sys


def ulam(n: int, sequence: list) -> list:
    sequence.append(n)
    if n == 1:
        return sequence
    if n % 2 == 0:
        new = n // 2
        ulam(new, sequence)
    else:
        new = n * 3 + 1
        ulam(new, sequence)
    return sequence


if __name__ == '__main__':

    integer = int(input())

    sequence: list = []

    resultl = ulam(integer, sequence)

    result = ''

    for i in range(len(resultl)):
        result += str(resultl[i]) + ' '

    print(result.rstrip())
