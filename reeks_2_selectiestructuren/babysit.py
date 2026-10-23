


def berekenBedrag(beginUur, beginMinuut, eindUur, eindMinuut):
  resultaat = 0

#19:10 - 20:40

  if (beginUur >= 18 & eindUur < 21 | (eindUur == 21 & eindMinuut <=30)):
    tijdInMinuten = (eindUur *60 + eindMinuut) - (beginUur * 60 + beginMinuut)
    resultaat += (tijdInMinuten / 60) * 2

  elif ((eindUur > 21 & eindMinuut > 30) & (beginUur >= 18 & beginUur < 21 | beginUur == 21 & beginMinuut <= 30)):
    tijdInMinuten = (eindUur * 60 + eindMinuut) - (beginUur * 60 + beginMinuut)
    resultaat += 



    
  


beginUur = int(input())
beginMinuut = int(input())
eindUur = int(input())
eindMinuut = int(input())



if beginUur > eindUur or (beginUur == eindUur and beginMinuut > eindMinuut):
  print("ongeldige invoer")

berekening = berekenBedrag(beginUur, beginMinuut, eindUur, eindMinuut)

if (berekening):
  print(berekening)
else:
  print("De babysitter is niet beschikbaar")

  


