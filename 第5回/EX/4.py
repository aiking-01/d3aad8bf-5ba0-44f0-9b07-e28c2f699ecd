import random
o=ord
print(t:=''.join([chr(random.randint(o('a'),o('z'))) for _ in range(5)]))
u=input('文字列を入力してください：')
print([f'誤りがあります。\n正解の文字列:{t}\nユーザーの文字列:{u}','正しく入力できています。'][u==t])