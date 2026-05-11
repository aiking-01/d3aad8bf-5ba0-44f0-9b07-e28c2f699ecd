'''
繰り返し
繰り返しをするための構文は、for文とwhile文の2種類があります。
for文は繰り返す回数が決まっているときに使います。
while文は繰り返す回数が決まっていないときに使います。
'''

'''
for文の書き方は
for 変数 in データ:
    繰り返す処理
です。
n回繰り返すときは、range(n)を使います。
'''
print('処理1')
for i in range(5):
    print(i)
print('\n')
'''
while文の書き方は
while 条件式:
    繰り返す処理
です。
条件式がTrueのときに繰り返す処理が実行されます。
'''
print('処理2')
i = 0
while i < 5:
    print(i)
    i += 1
print('\n')
'''
代入演算子
代入演算子は、変数に値を代入するための演算子です。
代入演算子には、+=、-=、*=、/=、//=、%=、**=があります。
これらは、直接変数の値を更新するために使用されます。
例えば、x += 1は、x = x + 1と同じ意味です。
'''
print('処理3')
x = 0
print(f'x:{x}')
x += 1
print(f'x:{x}')
print('\n')
'''
break文とcontinue文
break文は、繰り返しを中断するための文です。
continue文は、現在の繰り返しをスキップして、次の繰り返しに移ります。
'''
print('処理4')
for i in range(5):
    if i == 3:
        break
    print(i)
print('\n')

print('処理5')
for i in range(5):
    if i == 3:
        continue
    print(i)
print('\n')