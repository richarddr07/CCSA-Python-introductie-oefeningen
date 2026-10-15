aantalAppels = int(input())

aantalPaletten = aantalAppels // 20 // 35

aantalOverigeKisten = (aantalAppels // 20 % 35)

aantalOverigeAppels = aantalAppels % 20 

print(aantalPaletten)
print(aantalOverigeKisten)
print(aantalOverigeAppels)