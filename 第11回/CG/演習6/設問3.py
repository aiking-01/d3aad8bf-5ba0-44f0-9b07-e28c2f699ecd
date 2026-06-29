def dens(d,p):
 if p=="全体":
  j=m=0
  for _,b,c in d.values():j+=b;m+=c
 else:j,m=d[p][1],d[p][2]
 return j/m

print(dens(pref_dict, "全体")) # type: ignore