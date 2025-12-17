import json

with open('produkty.json', 'r', encoding='UTF-8') as file:
    data = json.load(file)

products = data["produkty"]

expProducts = [p for p in products if p["cena"] > 50]

res = {"produkty": expProducts}

with open('new.json', 'w', encoding='UTF-8') as out:
    json.dump(res, out, ensure_ascii=False, indent=4)
