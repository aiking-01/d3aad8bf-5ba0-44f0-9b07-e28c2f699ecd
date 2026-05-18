n_a = ord('a')
n_z = ord('z')
f = ''
length = 5
import random
for _ in range(length):
  n = random.randint(n_a,n_z)
  txt += chr(n)
print(txt)
input_txt = input('文字列を入力してください：')
if txt == input_txt:
  print('正しく入力できています。')
else:
  print('誤りがあります。')
  print(f'正解の文字列:{txt}')
  print(f'ユーザーの文字列:{input_txt}')