def clock():
    hour, minute, second = now()  # type: ignore
    return f"{hour+9}時{minute}分{second}秒"
print(clock())