import math

a = float(input())
b = float(input())
c = float(input())

D = b**2 - 4*a*c

if D < 0:
  print("geen wortels")
elif D ==  0:
  print("een wortel")
  print(f'{-b/2*a}')
else: 
  print("twee wortels")
  w1 = (-b - math.sqrt(D)) / (2*a)
  w2 = (-b + math.sqrt(D)) / (2*a)
  if (w1 < w2):
    print(w1)
    print(w2)
  else:
    print(w2)
    print(w1)


