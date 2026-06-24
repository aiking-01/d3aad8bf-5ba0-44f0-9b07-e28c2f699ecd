#---1---
import random
def dice5():return[random.randint(1,6)for _ in range(5)]
def judge0(l):return'凶吉'[sum(l)>=20]
print(dice5(),*[judge0(i)for i in[[10,11],[10,9],dice5()]],sep='\n')


#---2---
def judge1(l):return'吉大'[:min(max(l.count(i)for i in l),3)-1][::-1]
print(*[judge1(i)for i in[[1,1,1,2,3],[1,1,2,3,4],[1,2,3,4,5]]],sep='\n')


#---3---
def omikuji():
    if not (r:=judge1(l:=dice5())):r=judge0(l)
    return l,r


#---4---
import matplotlib.pyplot as p,japanize_matplotlib
p.bar(k:=['大吉','吉','凶'],[[omikuji()[1]for _ in range(100)].count(i)for i in k])
for i in[f'title("おみくじ100回の{(y:='結果")')}',f'x{(x:='label("')}{y}',f'y{x}回数")','show()']:eval('p.'+i)