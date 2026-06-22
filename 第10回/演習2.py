import random
def lot():
  selection = ['大吉', '吉', '中吉', '小吉', '末吉', '凶', '大凶']
  select = selection[random.randint(0, 6)]
  return select
print(lot())