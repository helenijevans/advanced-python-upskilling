import json


def saveDictionary(dict, filepath):
    with open(filepath, "w+") as f:
        f.write(json.dumps(dict))


dict = {
    "dfd": 5,
    "kk": 15,
}

saveDictionary(dict, "save_dict.txt")


def getDictionary(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
        print(data)


getDictionary("save_dict.txt")

"""
GIVEN SOLUTION
"""
# Same thing but using pickle.dump instead of json
