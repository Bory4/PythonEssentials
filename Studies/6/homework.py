#!/bin/python

class Ladunek:
    def __init__(self, nazwa, waga):
        self._nazwa = nazwa
        self.waga = waga

    @property
    def waga(self):
        return self._waga

    @waga.setter
    def waga(self, wartosc):
        if wartosc <= 0:
            raise ValueError("Akceptuję wyłącznie wartości dodatnie, postaraj się bardziej")
        self._waga = wartosc

    @property
    def nazwa(self):
        return self._nazwa

    def info(self):
        return f"Ładunek: {self.nazwa}, Waga: {self.waga} kg"

    def __add__(self, other):
        if not isinstance(other, Ladunek):
            return NotImplemented
        nowa_nazwa = f"Zestaw: {self.nazwa} + {other.nazwa}"
        nowa_waga = self.waga + other.waga
        return Ladunek(nowa_nazwa, nowa_waga)

    def __str__(self):
        return self.info()


class LadunekNiebezpieczny(Ladunek):
    def __init__(self, nazwa, waga, poziom_ryzyka):
        super().__init__(nazwa, waga)
        self.poziom_ryzyka = poziom_ryzyka

    def info(self):
        info = super().info()
        return f"{info} (! RYZYKO: {self.poziom_ryzyka} !)"


class LadunekZywnosc(Ladunek):
    def __init__(self, nazwa, waga, data_waznosci):
        super().__init__(nazwa, waga)
        self.data_waznosci = data_waznosci

    def info(self):
        info = super().info()
        return f"{info}, Data ważności: {self.data_waznosci}"


if __name__ == "__main__":
    try:
        ladunek1 = Ladunek("Prototypowe części dronów", 496)
        ladunek2 = LadunekNiebezpieczny("Paliwo jądrowo-jonowo-nuklearne", 12000, "Wysoki/B. Wysoki")
        ladunek3 = LadunekZywnosc("Racje żywnościowe dla sierot", 300, "2077-12-01")
    except ValueError as e:
        print(f"Błąd tworzenia ładunku: {e}")

    lista_ladunkow = [ladunek1, ladunek2, ladunek3]

    for ladunek in lista_ladunkow:
        print(ladunek)

    zestaw = ladunek1 + ladunek3
    print("Wynik dodawania (Części + Żywność):")
    print(zestaw)