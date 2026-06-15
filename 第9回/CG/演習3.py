def is_prime(n):return not{n%i for i in range(2,n)}&{0}
print(is_prime(44379667))