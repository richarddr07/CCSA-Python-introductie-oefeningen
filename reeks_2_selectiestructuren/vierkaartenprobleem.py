zijde = input()
omschrijving = input()
antwoord = input()

if zijde == "kleur":
    if omschrijving == "bruin":
        juisteAntwoord = "ja"
    else:
        juisteAntwoord = "nee"
else:
    if omschrijving == "8":
        juisteAntwoord = "ja"
    else:
        juisteAntwoord = "nee"

if juisteAntwoord == "ja":
    tekst = "moeten gedraaid worden"
else:
    tekst = "moeten niet gedraaid worden"

if antwoord == juisteAntwoord:
    resultaat = "Juist"
else:
    resultaat = "Fout"

print(f"{resultaat}: kaarten met {zijde} {omschrijving} {tekst}.")