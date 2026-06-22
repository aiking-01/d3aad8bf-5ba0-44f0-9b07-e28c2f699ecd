import math
def judge(x, y):
    distance = math.sqrt(x**2 + y**2)
    if distance <= 0.3:
        return True
    else:
        return False
print(judge(0.2, 0.2))   # True
print(judge(0.2, 0.3))   # False