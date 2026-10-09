notas=float(input("¿que notas has sacado?\n\n"))

if notas < 0 or notas > 10:
  print("incorrecto")
elif notas < 5:
    print("insuficiente")

elif notas >= 5  and notas < 6:
     print("suficiente")

elif notas >= 6 and notas < 7:
     print("Bien")

elif notas >= 7 and notas < 8:
     print("notable")

elif notas >= 9 and notas < 10:
     print("sobresaliente")





