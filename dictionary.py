# Maak een dictionary van je hobby met zoveel mogelijk datatypes

hobby = {
  "Hobby": "3D Printen",
  "Kosten": 200,
  "Inkomsten": 500.50,
  "Winstgevend" : True,
  "Zoektermen": ["3D Printen", "Printen", "Plastic", "Prototype"]
}

print("\n")

for key, value in hobby.items():
  
  if isinstance(value, list):
    print("{}: {}").format(key, str(value)[1:-1])
  else:
    print("{}: {}").format(key, value)

print("\n")