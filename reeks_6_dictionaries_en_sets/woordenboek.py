def vertaling_toevoegen(woord, vertaling, dict):
  dict[woord] = vertaling

def vertaling(woord, dict):
  if woord in dict:
    return dict[woord]
  else: 
    return '???'

woordenboek = {}
vertaling_toevoegen('plerzs', 'vrouw', woordenboek)
vertaling_toevoegen('nirtu', 'bloem', woordenboek)
vertaling_toevoegen('klinzoj', 'dorst', woordenboek)
vertaling_toevoegen('tilza', 'hond', woordenboek)
vertaling_toevoegen('zraidi', 'tijd', woordenboek)

print(woordenboek)

print(vertaling('tilza', woordenboek))
print(vertaling('guoles', woordenboek))
