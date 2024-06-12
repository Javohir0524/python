capitals = {"USA": "Washington D.C",
            "india": "New Delhi",
            "Uzbekistan": "Tashkent",
            "South Korea": "Seoul"}
#print(dir(capitals))
#print(help(capitals))
#print(capitals.get("India"))
if capitals.get("Uzbekistan"):
    print("That capital exists.")
else:
    print("That capital doesn't exist.")
