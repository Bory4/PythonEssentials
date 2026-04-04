def czyPierwsza(liczba):
    if liczba == 1:
        return False
    if liczba == 2:
        return True
    for i in range(2,liczba):
        if liczba % i == 0:
            return False
    return True

pierwsze = []

for i in range(1, 1000):
    if czyPierwsza(i):
        pierwsze.append(i)

print(pierwsze)

# O(N^2)