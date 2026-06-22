import random
def geta():
    rand = random.random()
    if rand < 0.3:
        return '晴れ'
    elif rand < 0.8:
        return '曇り'
    else:
        return '雨'
print(geta())