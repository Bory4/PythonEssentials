import csv

with open('dane.csv', 'r', encoding='utf-8') as file:
    data = csv.reader(file, delimiter=';')
    
    data = list(data)

colnames = data[0]
print("Columns names: ", colnames)

first_5 = data[1:6]

print("First 5 records: ")
for i in first_5:
    print(i)
    