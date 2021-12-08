import ujson

with open("example.json", "r") as f:
    file_json = ujson.load(f)

#print(file_json)
#print(type(file_json))

# for k, v in file_json.items():
#     print(k, v)

def crate_list_hobbies(hobbies):
    xx=0
    for x in hobbies:
        xx += 1
        print(xx, x)

def crate_list_children(children):
    xxx = 0
    for xx in children:
        xxx += 1
        print(xxx)
        for k, v in xx.items():
            print(k, v)



for k, v in file_json.items():
    if k != "hobbies" and k != "children":
        print(v)

    if k == "hobbies":
        print("hobbies count:",  len(v))
        crate_list_hobbies(v)

    if k == "children":
        print("children count:", len(v))
        crate_list_children(v)