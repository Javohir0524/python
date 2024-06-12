capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "Uzbekistan": "Tashkent",
            "South Korea": "Seoul"}

#capitals.update({"Germany": "Berlin"})
#capitals.update({"USA": "Detroit"})
#capitals.pop("China")
#capitals.popitem()
#capitals.clear()

#key = capitals.keys()
#for key in capitals.keys():
  #print(key)

# values = capitals.values()
#for value in capitals.values():
#print(value)

#items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")


