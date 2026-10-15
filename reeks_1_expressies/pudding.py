aantalGekocht = int(input())
kostprijsPerStuk = float(input())
aantalBarcodesNodig = int(input())
aantalMijlen = int(input())

print(f"Phillips spendeerde ${aantalGekocht * kostprijsPerStuk} voor {(aantalGekocht // aantalBarcodesNodig) * aantalMijlen} frequent flyer mijlen.")