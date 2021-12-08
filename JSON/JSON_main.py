import ujson


# to file JSON
class Tournament:
    def __init__(self, name, year):
        self.name = name
        self.year = year


tournament = {
    "S7": 2012,
    "Uralskie": 2022,
    "Aeroflot": 2010
}
json_data = ujson.dumps(tournament, indent=2) # serialization
print(json_data)
with open("example2.json", "w") as f:
    f.write(json_data)

# read file json
with open("example2.json", "r") as f:
    load_json = f.read()
    print(load_json)



