n = int(input('整数を入力:'))
for i in range(n):
  if n % i == 0:
    print('素数ではない')
else:
  print('素数')