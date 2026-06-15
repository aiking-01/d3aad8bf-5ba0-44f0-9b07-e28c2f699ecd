primes = []
for i in range(2,21):
    if is_prime(i): # type: ignore
        primes.append(i)
print(primes)