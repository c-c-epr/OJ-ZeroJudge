t=int(input())
for _ in range(t):
  an=list(map(int,input().split()))
  
  # 等比
  if an[1]-an[0]==an[2]-an[1]:
    an.append(an[3]+(an[1]-an[0]))
  # 等差
  else:
    an.append(an[3]*(an[3]//an[2]))
  print(*an)
  
