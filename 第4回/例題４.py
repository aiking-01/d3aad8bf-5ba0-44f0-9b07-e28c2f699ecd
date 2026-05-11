n = int(input('整数を入力:'))
count = 0
for i in range(2, n):
  if n % i == 0:
    count += 1
if count > 0:
  print('素数ではない')
else:
  print('素数')