import json
import os

def readJSON(filepath):
    with open(filepath, encoding='utf-8-sig') as file:
        data = json.load(file)
        file.close()
    return data['data']

def buildJSON(path):
    array = []
    for filepath in os.listdir(path="data"):
        print(filepath)
        data = readJSON(path+'/'+filepath)
        for string in data:
            array.append(string["d"])
    return {'data': array} # возвращает словарь под запись в json

def writeDataJSON(dictionary):
    with open('data.json', 'w') as f:
        json.dump(dictionary, f)