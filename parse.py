import json
import os
import datetime

def readDataJSON(filepath):
    with open(filepath, encoding='utf-8-sig') as file:
        data = json.load(file)
        file.close()
    return data['data']

def buildDataJSON(path):
    array = []
    for filepath in os.listdir(path="data"):
        print(filepath)
        data = readDataJSON(path+'/'+filepath)
        for string in data:
            array.append(string["d"])
    return {'data': array} # возвращает словарь под запись в json

def buildDateJSON(data):
    array = []
    for date in data:
        date += 1138752000
        array += timestampToDate(date)
        return {'date': array} # возвращает словарь под запись в json


def writeDataJSON(dictionary):
    with open('data.json', 'w') as f:
        json.dump(dictionary, f)

def timestampToDate(timestamp):
    return str(datetime.datetime.fromtimestamp(timestamp))[:7]