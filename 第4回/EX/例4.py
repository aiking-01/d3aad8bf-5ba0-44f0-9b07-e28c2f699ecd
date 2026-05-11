from sympy import sieve
print(f'素数{'' if int(input('整数を入力:')) in sieve else 'ではない'}')