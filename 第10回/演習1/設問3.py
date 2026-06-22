for i in range(1,6):
    x,y=target_pos() # type: ignore
    if judge(x,y): # type: ignore
        print(f'{i}回目: あたり')
    else:
        print(f'{i}回目: はずれ')