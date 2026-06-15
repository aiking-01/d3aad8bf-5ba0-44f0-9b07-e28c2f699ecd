def P(n):
    s=[0]*2+[1]*(m:=n**2)
    for i in range(2,m):
        if s[i]:
            for j in range(i*i,m,i):
                s[j]=0
    return [i for i in range(len(s)) if s[i]]
print(P(10))