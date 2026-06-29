def primes(n):
    prime_list = []
    for num in range(2, n + 1):
        if is_prime(num):  # type: ignore
            prime_list.append(num)
    return prime_list
print(len(primes(100)))