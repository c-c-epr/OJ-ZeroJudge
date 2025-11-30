from math import sqrt
a,b,c=map(int,input().split())

# 判別式
D=b**2-4*a*c

if D>0:
  print(f'Two different roots x1={int((-b+sqrt(D))//(2*a))} , x2={int((-b-sqrt(D))//(2*a))}')
elif D==0:
    print(f'Two same roots x={-b//(2**a)}')
else:
    print("No real root")
