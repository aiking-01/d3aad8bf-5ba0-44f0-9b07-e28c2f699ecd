count = 0
nums = 0
while True:
  num = int(input('整数を入力:'))
  nums += num
  count += 1
  if num == 0:
    break
print(f'平均は{nums / count}')