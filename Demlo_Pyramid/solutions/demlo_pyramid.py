import sys


def demlo_pyramid_maker(n: int):
    if n != 0:
        for i in range(1, n + 1):
            print((int('1'*i))**2)


if __name__ == '__main__':

    levels = int(input())

    demlo_pyramid_maker(levels)
