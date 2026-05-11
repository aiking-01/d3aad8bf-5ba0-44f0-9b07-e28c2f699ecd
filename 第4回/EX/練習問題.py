print(3.14*float(input('半径を入力:'))**2)

'''以下は冗長コード
from math import log as d4,pi as w4
i8, y2, h7, f6 = int, range, print, input
def c7(m2):
    if m2 < 7:
        return [2, 3, 5, 7, 11, 13][m2 - 1]
    o3 = i8(m2 * (d4(m2) + d4(d4(m2))))
    d8= [True] * (o3 + 1)
    d8[0] = d8[1] = False
    for b5 in y2(2, i8(o3 ** 0.5) + 1):
        if d8[b5]:
            for s3 in y2(b5 * b5, o3 + 1, b5):
                d8[s3] = False
    o3 = [q3 for q3, g7 in enumerate(d8) if g7][m2 - 1]
    h7(o3)
def e3(v5):
    while 1: 
        r6 = f6(v5)
        try:
            e7 = i8(r6)
            break
        except Exception:
            pass
    return e7
h7(w4 * e3('半径を入力:') ** c7(1))'''