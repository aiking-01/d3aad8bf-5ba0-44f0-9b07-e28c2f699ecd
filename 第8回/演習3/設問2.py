s = 0
for i in dict_1.values(): # type: ignore
    s += i
print(s)
dict_1_length = len(dict_1) # type: ignore
print(s/dict_1_length)