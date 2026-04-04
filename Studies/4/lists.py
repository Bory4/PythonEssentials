# Lists
a = list(range(1,21))

for i in a:
    if i % 2 == 0:
        print(i)


names = ["Zofia", "Adam", "Kamil", "Beata"]
names.sort()
print(names)

temp = 0
for i in range(0,5):
    num = int(input("Podaj liczbę: "))
    temp += num

temp = temp/5
print(temp)
