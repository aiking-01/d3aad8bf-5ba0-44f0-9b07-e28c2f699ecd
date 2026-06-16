def Sieve_of_Eratosthenes(n):
    if n < 1:
        return []
    p = (n + 1) ** 2
    s = [True] * p
    s[0] = False
    s[1] = False
    for i in range(2, p):
        if s[i]:
            for j in range(i * i, p, i):
                s[j] = False
    primes = []
    for i in range(2, p):
        if s[i]:
            primes.append(i)
        if len(primes) == n:
            break
    return primes
for i in range(1, 11):
    print(Sieve_of_Eratosthenes(i))
print(len(Sieve_of_Eratosthenes(1000)))