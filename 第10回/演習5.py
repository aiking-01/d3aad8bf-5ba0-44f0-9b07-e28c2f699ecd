#---1---
import random
def dice5():
    randlist = []
    for i in range(5):
        randlist.append(random.randint(1, 6))
    return randlist

def judge0(l):
    total = sum(l)
    if total >= 20:
        return '吉'
    else:
        return '凶'

print(dice5())
print(judge0([10, 11]))
print(judge0([10, 9]))
print(judge0(dice5()))



#---2---
def judge1(l):
    count = [0] * 7
    for i in l:
        count[i] += 1
    max_count = max(count)
    if max_count >= 3:
        return '大吉'
    elif max_count == 2:
        return '吉'
    else:
        return ''

print(judge1([1, 1, 1, 2, 3]))
print(judge1([1, 1, 2, 3, 4]))
print(judge1([1, 2, 3, 4, 5]))



#---3---
def omikuji():
    l = dice5()
    result = judge1(l)
    if result == '':
        result = judge0(l)
    return l, result

print(omikuji())



#---4---
import matplotlib.pyplot as plt
import japanize_matplotlib
count = {'大吉': 0, '吉': 0, '凶': 0}

for _ in range(100):
    _, result = omikuji()
    count[result] += 1

print(count)

plt.bar(count.keys(), count.values())
plt.title("おみくじ100回の結果")
plt.xlabel("結果")
plt.ylabel("回数")
plt.show()