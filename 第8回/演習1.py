alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a_list = list(alphabet)      # これで、 a_list = ['A', 'B', 'C', ... , 'Z']  と同じ効果が得られる
print(a_list)

# 以下に、「アルファベットの 3 番目は C です」のようにすべてのアルファベットを表示するプログラムを作成しなさい。
for i,x in enumerate(a_list):
    print(f'アルファベットの{i+1}番目は{x}です')