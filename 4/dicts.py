dictionary ={
    "Poland":"Warsaw",
    "Germany":"Berlin",
    "Russia":"Moscov"
}

country = input("Give me name of a country! ")
try:
    print(dictionary[country])
except:
    pass
chars = {}

for i in country:
    if i in chars:
        chars[i] += 1
    else:
        chars[i] = 1

print(chars)

grades = {
    "History" : 3,
    "IT" : 6,
    "Polish" : 3
}
print(f"Avg {sum(grades.values()) / len(grades)}")