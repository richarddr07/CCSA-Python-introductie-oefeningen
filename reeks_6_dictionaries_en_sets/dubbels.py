def dubbel(lijst):
  voorkomenVanElementen = {}
  for el in lijst:
    if (el in voorkomenVanElementen):
      voorkomenVanElementen[el] += 1
    else:
      voorkomenVanElementen[el] = 1
  for k, v in voorkomenVanElementen.items():
    if (v > 1):
      return k
  return None

print(dubbel([1,2,3,4,2]))
print(dubbel([1,2,3,4]))
print(dubbel([1,2,3,4,5,6,100,-234,15,0,-20000,15]))
    


def dubbels(lijst):
  eenmaal = set()
  meermaals = set()
  voorkomenVanElementen = {}

  for el in lijst:
    if el in voorkomenVanElementen:
      voorkomenVanElementen[el] += 1
    else:
      voorkomenVanElementen[el] = 1

  for k, v in voorkomenVanElementen.items():
    if (v > 1):
      meermaals.add(k)
    else:
      eenmaal.add(k)

  return eenmaal, meermaals





print(dubbels([1, 2, 3, 4, 2]))
print(dubbels([2, 8, 8, 6, 10, -20, -4, -2, -4]))
print(dubbels([1, 3, 5, 7, 2, 4, 6]))
