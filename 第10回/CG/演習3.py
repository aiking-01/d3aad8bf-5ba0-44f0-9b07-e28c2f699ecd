import random
def geta():return '晴曇雨れり'[random.choices(range(3),[0.3,0.5,0.2])[0]::3]
print(geta())