from random import random as r
def target_pos():return (r()-0.5,r()-0.5)
x,y=target_pos()
print(f'座標は {x=:6.3f}, {y=:6.3f} です')