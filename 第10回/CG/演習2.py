import random
def lot():return'大中小末大凶吉吉吉吉吉凶'[random.randint(0,6)::6]
print(lot())