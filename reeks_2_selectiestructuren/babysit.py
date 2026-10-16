beginUur = int(input())
beginMinuut = int(input())
eindUur = int(input())
eindMinuut = int(input())

if beginUur > eindUur or (beginUur == eindUur and beginMinuut > eindMinuut):
  print("ongeldige invoer")


def berekenBedrag(beginUur, beginMinuut, eindUur, eindMinuut):
  #TODO

berekening = berekenBedrag(beginUur, beginMinuut, eindUur, eindMinuut)

if (berekening):
  print(berekening)
else:
  print("De babysitter is niet beschikbaar")

  


