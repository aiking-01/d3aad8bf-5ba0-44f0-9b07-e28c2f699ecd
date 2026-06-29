count = 0
for i in range(101):
    if is_prime(i): # type: ignore
        count += 1
print(count)