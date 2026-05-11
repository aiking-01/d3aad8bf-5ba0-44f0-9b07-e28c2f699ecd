L=[1]
while L[-1]:L.append(int(input('整数を入力:')))
del L[0],L[-1];print(f'平均は{sum(L)/len(L)}')