try:
    file = open("dane.txt", encoding="UTF-8").read().strip().split("\n")

except FileExistsError as e:
    print(e)
    exit()
except FileNotFoundError as e:
    print(e)
    exit()
print(f"Łączna liczba lini w pliku: {len(file)}")

temp = []

for i in file:
    j = i.split(" ")
    for k in j:
        if k != "":
            temp.append(k)

print(f"Łączna liczba słów w pliku: {len(temp)}")

temp = 0

for i in file:
    temp += len(i)

print(f"Łączna liczba wszystkich znaków: {temp}")