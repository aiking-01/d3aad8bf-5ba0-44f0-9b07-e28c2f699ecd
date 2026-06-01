import itertools as a ,math
print(sum([-int(50/-math.prod(j))for i in range(4)for j in a.combinations([-2,-3,-5],i)]))