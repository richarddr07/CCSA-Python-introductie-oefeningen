gebaar1 = input()
gebaar2 = input()

if gebaar1 == "blad":
  if gebaar2 == "schaar":
    print("speler2 wint")
  elif gebaar2 == "steen":
    print("speler1 wint")
  elif gebaar2 == "hagedis":
    print("speler2 wint")
  elif gebaar2 == "spock":
    print("speler1 wint")

if gebaar2 == "blad":
  if gebaar1 == "schaar":
    print("speler1 wint")
  elif gebaar1 == "steen":
    print("speler2 wint")
  elif gebaar1 == "hagedis":
    print("speler1 wint")
  elif gebaar1 == "spock":
    print("speler2 wint")

if gebaar1 == "spock":
  if gebaar2 == "hagedis":
    print("speler2 wint")
  if gebaar2 == "schaar":
    print("speler1 wint")



