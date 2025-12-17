import csv
import json

with open('dane.csv', 'r', encoding='utf-8') as file:
    data = csv.reader(file, delimiter=';')
    
    data = list(data)

headers = data[0]
data = data[1:]

temp = []

for i in data:
    osoba = {
        'Imię': i[0],
        'Wiek': i[1],
        'Miasto' : i[2]
    }

    temp.append(osoba)

temp = {"Osoba":temp}

with open('converted.json', 'w', encoding='UTF-8') as out:
    json.dump(temp, out, ensure_ascii=False, indent=4)

print(data)
