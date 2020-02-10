# Invoer 2 getallen, eerste getal delen door tweede getal.
failed = True

while failed:
  getal1 = float(input("Voer het eerste getal in: "))
  getal2 = float(input("Voer het tweede getal in: "))
  try:
    print(str(getal1) + " gedeeld door " + str(getal2) + " is " + str(getal1 / getal2))
    failed = False
  except:
    print("Geen geldige invoer. \nProbeer het opnieuw. \n")
    failed = True