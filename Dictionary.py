# Python Dictionaries
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.


# Dictionary Methods
# Python has a set of built-in methods that you can use on dictionaries.
#
# Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary


dictFord = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dictFord["brand"], dictFord["model"], dictFord["year"])
print(dictFord.get("model"))

thisdict = {
  "ff": 112,
  "Facel Vega": 122,
  "Faraday Future": 162,
  "FAW": 125,
  "Ferrari": 142,
  "Fiat": 12,
  "Fioravanti": 12,
  "Fisker": 12,
  "Foden Trucks": 12,
  "Force Motors": 12,
  "Ford": 12,
  "Foton": 12,
  "FPV": 12,
  "Franklin": 12,
  "Freightliner": 12
}

thisdict2 = dict(Eagle=3, EDAG=5, Edsel=2, Eicher=7, Elemental=6, Elfin=2, Elva=1, Englon=8, ERF=11, Eterniti=32,
                 Auto=33)
print(thisdict2)
top1 = thisdict2["Eagle"]
top2 = thisdict2.get("Elemental")
print(top1, top2)
thisdict2["ERF2"] = 456  # add to thisdict2
print(thisdict2)

thisdict3 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict3["colors"])
for entry in thisdict3["colors"]:
  print(entry)

print(f"Key {thisdict.keys()}")  # Key dict_keys(['ff',......
print(f"Value {thisdict.values()}")  # Value dict_values([12,....

print(f"Key List{list(thisdict.keys())}")  # Key dict_keys(['ff',......
print(f"Value List {list(thisdict.values())}")  # Key dict_keys(['ff',......

print("Ferrari" in thisdict)
print("Ferrari" not in thisdict)

thisdict3_copy = thisdict3.copy()
print(thisdict3_copy)

for k, v in thisdict3_copy.items():
  print(k, v)
