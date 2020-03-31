import json

def parseJSON(path):
    with open(path, encoding='utf-8-sig') as file:
        data = json.load(file)
        file.close()
    return data['data']

