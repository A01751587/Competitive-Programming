import sys


def reverse(word: str):
    for i in range(len(word) - 1, -1, -1):
        spaces = ' ' * (i)
        print(spaces + word[i:])


if __name__ == '__main__':

    word = input()

    reverse(word)
