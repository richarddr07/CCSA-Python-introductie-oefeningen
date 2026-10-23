def iszigzag(geheleGetallen):
  isZigZag = True

  vorigeIndex = -1
  for i in range(len(geheleGetallen) - 1):
    if (vorigeIndex != -1 | i != len(geheleGetallen) - 1): 
      if (i % 2 == 0): #in geval van even index
        isZigZag = geheleGetallen[i] > geheleGetallen[vorigeIndex]
      else:
        isZigZag = geheleGetallen[i] < geheleGetallen[vorigeIndex]
   
    vorigeIndex = i # vooraleer lus verlaten vorigGetal op huidige index zetten

    if (isZigZag == False): # Lus stopzetten vanaf één keer False wordt waargenomen
      break


  return isZigZag

def zigzag_traag(geheleGetallen):

  geheleGetallen.sort()

  for i in range(len(geheleGetallen)):
    if ((i != 0 and i != len(geheleGetallen) - 1) and i % 2 != 0): #Niet 1ste of laatste + oneven
      wissel = geheleGetallen.pop(i)
      geheleGetallen.insert(i-1, wissel)

def zigzag_snel(geheleGetallen):
    for i in range(0, len(geheleGetallen), 2):
        if i > 0 and geheleGetallen[i] < geheleGetallen[i - 1]:
            geheleGetallen[i], geheleGetallen[i - 1] = geheleGetallen[i - 1], geheleGetallen[i]
        if i < len(geheleGetallen) - 1 and geheleGetallen[i] < geheleGetallen[i + 1]:
            geheleGetallen[i], geheleGetallen[i + 1] = geheleGetallen[i + 1], geheleGetallen[i]

print(iszigzag([10,5,6,3,2,20,100,80]))

print(iszigzag([10,5,6,2,20,3,100,80]))

print(iszigzag([20,5,10,2,80,6,100,3]))

reeks = [10,90,49,2,1,5,23]
zigzag_traag(reeks)
print(reeks)

reeks = [10,90,49,2,1,5,23]
zigzag_snel(reeks)
print(reeks)


  













      








    
