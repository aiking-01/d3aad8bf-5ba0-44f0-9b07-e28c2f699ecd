import random

def target_pos():
    loc_x = random.random() - 0.5
    loc_y = random.random() - 0.5
    return (loc_x, loc_y)

x, y = target_pos()

print(f'座標は x={x:6.3f}, y={y:6.3f} です')