import json

json_file = "../JSON/Person.json"


def write_json(date, json_file=json_file):
    with open(json_file, "w") as jf:
        json.dump(date, jf, indent=4)






def add_person_with_json_file(id, name, age, father):
    with open(json_file) as jf:
        date = json.load(jf)
        temp = date["persons"]
        temp.append({"id": id, "name": name, "age": age, "father": father})
        write_json(date)


add_person_with_json_file(4, "fatema", 88, "omar")
