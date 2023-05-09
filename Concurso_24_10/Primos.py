
def prime_range(n):
    primes = [2]
    for i in range(3, n+1):
        for p in primes:
            if i % p == 0 or p * p > i:
                break
        else:
            primes.append(i)
    return primes


def primos(n: int) -> str:
    if n < 2:
        return "NO CUENTO"
    lim = int(n ** .5)
    for i in range(2, lim + 1):
        if n % i == 0:
            return "COMPUESTO"
    return "PRIMO"


if __name__ == '__main__':
    s = input()

    print(primos(int(s)))
