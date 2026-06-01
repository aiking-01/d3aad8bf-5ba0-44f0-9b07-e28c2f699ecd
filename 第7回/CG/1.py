m=[len(c:=['Kobe', 'Osaka', 'Kyoto'])]
c+=['Nara']
for i in range(6):m+=[i]
for i in c:m+=[i]
print(*m,sep='\n')