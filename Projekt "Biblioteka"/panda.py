import pandas as pd

class Book:
    def __init__(self,title,author,year,isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
    def to_dict(self) -> dict:
        return {
            "title":self.title,
            "author":self.author,
            "year":self.year,
            "isbn":self.isbn
        }
        

# Krok 1: Tworzymy słownik z danymi książki. Ten fragment pozostaje bez zmian.
# Step 1: Create a dictionary with book data. This part remains unchanged.
panDadeusz = Book("tytul","autor",2137,69420).to_dict()

# ZMIANA 1: Usunięto zbędną inicjalizację DataFrame.
# CHANGE 1: Removed redundant DataFrame initialization.
# Linia `df = pd.DataFrame(columns=[...])` została usunięta, ponieważ tworzyła
# pusty DataFrame, który i tak był natychmiast nadpisywany kilka linii niżej.
# The line `df = pd.DataFrame(columns=[...])` was removed because it created
# an empty DataFrame that was immediately overwritten a few lines later anyway.

new_id = 1

# Krok 2: Modyfikujemy słownik.
# Step 2: Modify the dictionary.
# Linia `new_book_data = panDadeusz` nie tworzy kopii, a jedynie drugą nazwę
# dla tego samego słownika. Dla przejrzystości operujemy wprost na oryginale.
# The line `new_book_data = panDadeusz` doesn't create a copy, just a second name
# for the same dictionary. For clarity, we operate directly on the original.
panDadeusz['id'] = new_id 

print("Słownik po dodaniu ID:")
print(panDadeusz)

# Krok 3: Tworzymy DataFrame z listy zawierającej nasz jeden słownik.
# Step 3: Create the DataFrame from a list containing our single dictionary.
df = pd.DataFrame([panDadeusz])

# ZMIANA 2: Odkomentowano i aktywowano jawną kolejność kolumn.
# CHANGE 2: Uncommented and activated explicit column ordering.
# Ta linia jest kluczowa dla zapewnienia, że kolumny w DataFrame
# będą ZAWSZE w tej samej, oczekiwanej kolejności (`id` na początku),
# niezależnie od tego, jak wewnętrznie ułożone są klucze w słowniku.
# This line is key to ensuring that the columns in the DataFrame
# will ALWAYS be in the same, expected order (with `id` at the beginning),
# regardless of how the keys are internally arranged in the dictionary.
df = df[["id", "title", "author", "year", "isbn"]]

print("\nFinalny DataFrame z poprawną kolejnością kolumn:")
print(df)

# Zapis do pliku CSV. Użycie `index=False` jest bardzo ważne, aby pandas
# nie dodawał własnej, dodatkowej kolumny z indeksem (0, 1, 2...).
# Saving to CSV. Using `index=False` is very important so that pandas
# doesn't add its own extra index column (0, 1, 2...).
df.to_csv("novy.csv", index=False)