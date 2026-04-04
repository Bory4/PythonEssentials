def silnia(n):
    temp = 1
    for i in range(1, n+1):
        temp *= i
    return temp

print(silnia(5))

def czy_pierwsza(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(czy_pierwsza(7))

def odwroc_tekst(tekst):
    return tekst[::-1]