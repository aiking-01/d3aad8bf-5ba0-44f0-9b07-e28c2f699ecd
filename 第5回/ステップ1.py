n_a = ord('a')
n_z = ord('z')
f = ''
length = 5
import random
for _ in range(length):
  n = random.randint(n_a,n_z)
  txt += chr(n)