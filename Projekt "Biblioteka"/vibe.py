import pandas as pd

class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "isbn": self.isbn
        }

# Tworzymy słownik z danymi książki
book_data = Book("Pan Tadeusz", "Adam Mickiewicz", 2137, 9788373271810).to_dict()

# Dodajemy ID do słownika
new_id = 1
book_data['id'] = new_id 

print("Słownik z danymi książki:")
print(book_data)

# KLUCZOWA ZMIANA: Tworzymy DataFrame z LISTY zawierającej jeden słownik
df = pd.DataFrame([book_data])

# Opcjonalnie: Zmieniamy kolejność kolumn, aby 'id' było pierwsze
df = df[['id', 'title', 'author', 'year', 'isbn']]

print("\nPoprawnie utworzony DataFrame:")
print(df)

# Teraz zapis do CSV zadziała poprawnie
df.to_csv("booksv.csv", index=False)