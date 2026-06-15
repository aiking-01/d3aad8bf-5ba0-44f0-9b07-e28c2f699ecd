pets = [0, 0, 0, 1, 0, 0, 2, 0, 1, 3, 0, 0, 0, 2, 0, 1, 1, 0, 2, 0, 0, 1, 0]
count = {}
for i in set(pets):
    count[i] = pets.count(i)
print(count)