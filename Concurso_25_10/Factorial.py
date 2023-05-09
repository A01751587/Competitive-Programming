factorial_dict = {}


def factorial(n):
    if n < 2:
        return 1
    if n not in factorial_dict:
        factorial_dict[n] = n * factorial(n - 1)
    return factorial_dict[n]


def divisores(n: int) -> int:
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


if __name__ == '__main__':
    s = input()

    for i in range(1, int(s)):
        factorial(i)

    print(divisores(factorial(int(s))))
