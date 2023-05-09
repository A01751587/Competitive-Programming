def prime_range(n):
    primes = [2]
    for i in range(3, n+1):
        for p in primes:
            if i % p == 0:
                break
            elif p * p > i:
                primes.append(i)
                break
    return primes


if __name__ == '__main__':
    s = input()

    primes = prime_range(8000)

    print(primes[int(s) - 1])
