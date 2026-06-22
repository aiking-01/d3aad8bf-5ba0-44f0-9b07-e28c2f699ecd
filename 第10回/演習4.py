# 課題 1, 2 について、n人分のデータが入ったリストを作成して、できたことを確認しよう。
n = 30
import random
birthdays = []
for i in range(n):
    birthday = random.randint(1, 365)
    birthdays.append(birthday)
print(birthdays)


# 人数 n を引数にとる関数 has_same_bday(n) を作成しよう。（上で作ったコードを活用 … コピー: ctrl+C, ペースト: ctrl+V ）
# この関数は、n人分の誕生日データをランダムに生成し、
# 同じ誕生日の人が存在する場合は True、存在しない場合は False を返すものとする。
#    （誕生日データの要素数と集合（set）に変換した場合の要素数が異なっていれば、同じ要素が存在したことになります。）
def has_same_bday(n):
    birthdays = []
    for i in range(n):
        birthday = random.randint(1, 365)
        birthdays.append(birthday)
    birthdays_len = len(birthdays)
    birthdays_set_len = len(set(birthdays))
    if birthdays_len != birthdays_set_len:
        return True
    else:
        return False


# 30人のクラスの場合について、誕生日が同じ人が存在するかどうかを確認しよう。
print(has_same_bday(30))


# 作成した関数を100回実行し、誕生日が同じ人が存在した回数（True となった回数）を数えよう。
# そして、その回数をもとに、誕生日が同じ人が存在する割合を求めて表示しよう。
# さらに、実行回数を10000回に増やして同様に割合を求め、結果を表示しよう。

count = 0
for _ in range(10000):
    if has_same_bday(30):
        count += 1
print(f"誕生日が同じ人が存在する確率: {count / 10000 * 100}%")


