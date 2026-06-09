dict_2 = {}
name = input('名前:')
while name != 'End':
    money = int(input('所持金額:'))
    dict_2[name] = money
    name = input('名前:')
print(dict_2)