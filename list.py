# http://github.com/sjoerrdd/python-opdrachten
# Lijst met lijsten
# Rooster maken, 1-100. 1-10, 11-20

getallen = [list(range(i, i+10)) for i in range(1,100,10)] # list() i.p.v. [], anders worden de haakjes ook geprint.

for getal in getallen:
  print(" ".join(map(str, getal)))


# Lange versie:
# getallen = []
# for i in range(1, 100, 10):
#   getallen.append(list(range(i, i + 10))

# for getal in getallen:
#   print(" ".join(map(str, getal)))