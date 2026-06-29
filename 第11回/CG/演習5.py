def primes(n):return [i for i in range(2,n+1)if is_prime(i)] # type: ignore
print(len(primes(100)))