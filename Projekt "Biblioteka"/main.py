# --- Imports ---
import os
import pandas as pd # Importujemy tylko te biblioteki, których używamy

# --- Data Model / Model Danych ---
# Klasa Book jest teraz jeszcze prostsza - nie zarządza ID.
# The Book class is now even simpler - it doesn't manage IDs.
class Book:
    """
    Klasa reprezentująca pojedynczą książkę. Służy jako szablon i walidator.
    A class representing a single book. Serves as a template and validator.
    """
    def __init__(self, title: str, author: str, publication_year: int, status: str = "do przeczytania"):
        if not title or not author:
            raise ValueError("Tytuł i autor nie mogą być puste.")
        if not isinstance(publication_year, int) or publication_year <= 0:
            raise ValueError("Rok wydania musi być dodatnią liczbą całkowitą.")

        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.status = status

    def to_dict(self) -> dict:
        """
        Konwertuje obiekt na słownik (bez ID).
        Converts the object to a dictionary (without an ID).
        """
        return {
            "title": self.title,
            "author": self.author,
            "publication_year": self.publication_year,
            "status": self.status
        }

# --- Business Logic / Logika Biznesowa ---
class Library:
    """
    Zarządza kolekcją książek używając Pandas DataFrame.
    Manages the book collection using a Pandas DataFrame.
    """
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.columns = ["id", "title", "author", "publication_year", "status"]
        
        directory = os.path.dirname(self.filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        self.books_df = self.load_from_file()

    def load_from_file(self) -> pd.DataFrame:
        """
        Wczytuje dane z pliku CSV. Jeśli plik nie istnieje, tworzy pusty DataFrame.
        Loads data from a CSV file. If the file doesn't exist, creates an empty DataFrame.
        """
        if not os.path.exists(self.filepath):
            return pd.DataFrame(columns=self.columns)
        try:
            # Wczytujemy dane i upewniamy się, że kolumna 'id' jest typu integer
            # We load data and ensure the 'id' column is of integer type
            df = pd.read_csv(self.filepath)
            if 'id' in df.columns:
                 # Używamy Int64, aby uniknąć problemów z ewentualnymi brakami danych
                 # We use Int64 to avoid problems with potential missing data
                df['id'] = df['id'].astype('Int64')
            return df
        except pd.errors.EmptyDataError:
            return pd.DataFrame(columns=self.columns)

    def save_to_file(self):
        """
        Zapisuje DataFrame do pliku CSV bez indeksu pandas.
        Saves the DataFrame to a CSV file without the pandas index.
        """
        try:
            # Zapisujemy DataFrame do CSV. `index=False` bo ID jest już zwykłą kolumną.
            # We save the DataFrame to CSV. `index=False` because the ID is now a regular column.
            self.books_df.to_csv(self.filepath, index=False)
        except IOError:
            print(f"Błąd: Nie udało się zapisać danych do pliku {self.filepath}.")

    def add_book(self, book: Book):
        """
        Dodaje nową książkę, generując dla niej nowe, numeryczne ID.
        Adds a new book, generating a new numeric ID for it.
        """
        # --- NOWA LOGIKA GENEROWANIA ID ---
        # --- NEW ID GENERATION LOGIC ---
        if self.books_df.empty or self.books_df['id'].max() != self.books_df['id'].max(): # Drugi warunek sprawdza czy nie ma NaN
            new_id = 1
        else:
            new_id = self.books_df['id'].max() + 1
        
        new_book_data = book.to_dict()
        new_book_data['id'] = new_id  # Dodajemy wygenerowane ID do danych książki

        new_book_df = pd.DataFrame([new_book_data])
        self.books_df = pd.concat([self.books_df, new_book_df], ignore_index=True)
        
        self.save_to_file()
        print(f"Dodano książkę: {book.title} (ID: {new_id})")

    def display_all_books(self):
        """
        Wyświetla wszystkie książki, sortując je po ID.
        Displays all books, sorting them by ID.
        """
        if self.books_df.empty:
            print("Biblioteka jest pusta.")
        else:
            print("\n--- Lista Książek ---")
            # Ustawiamy 'id' jako tymczasowy indeks do ładnego wyświetlenia
            # We set 'id' as a temporary index for nice display formatting
            display_df = self.books_df.set_index('id')
            print(display_df.sort_index().to_string())
            print("---------------------\n")

    def search_books(self, query: str) -> pd.DataFrame:
        query = query.lower()
        results_df = self.books_df[
            self.books_df['title'].str.lower().str.contains(query, na=False) |
            self.books_df['author'].str.lower().str.contains(query, na=False)
        ]
        return results_df

    def remove_book(self, book_id: int) -> bool:
        """
        Usuwa książkę z DataFrame na podstawie jej numerycznego ID.
        Removes a book from the DataFrame based on its numeric ID.
        """
        # Sprawdzamy, czy ID w ogóle istnieje w kolumnie 'id'
        # We check if the ID exists in the 'id' column at all
        if book_id not in self.books_df['id'].values:
            print("Nie znaleziono książki o podanym ID.")
            return False

        # Zapisujemy tytuł do wyświetlenia
        # We save the title for display
        title_to_remove = self.books_df.loc[self.books_df['id'] == book_id, 'title'].iloc[0]
        
        # Usuwamy wiersze, gdzie wartość w kolumnie 'id' jest równa podanej
        # We remove rows where the value in the 'id' column equals the provided one
        self.books_df = self.books_df[self.books_df['id'] != book_id]
        
        self.save_to_file()
        print(f"Usunięto książkę: {title_to_remove}")
        return True

# --- User Interface & Main loop ---
def display_menu():
    print("\n=== CYFROWA DOMOWA BIBLIOTECZKA (Pandas, Auto-ID) ===")
    print("1. Pokaż wszystkie książki")
    print("2. Dodaj nową książkę")
    print("3. Wyszukaj książkę")
    print("4. Usuń książkę (po ID)")
    print("5. Zakończ")
    print("=" * 50)

def get_book_data() -> Book | None:
    # Ta funkcja pozostaje bez zmian
    try:
        title = input("Podaj tytuł: ")
        author = input("Podaj autora: ")
        while True:
            try:
                year_str = input("Podaj rok wydania: ")
                publication_year = int(year_str)
                break
            except ValueError:
                print("Błąd: Rok musi być liczbą. Spróbuj ponownie.")
        return Book(title=title, author=author, publication_year=publication_year)
    except ValueError as e:
        print(f"Błąd podczas tworzenia książki: {e}")
        return None

def main():
    data_folder = "data"
    filename = "library.csv"
    filepath = os.path.join(data_folder, filename)
    library = Library(filepath)

    while True:
        display_menu()
        choice = input("Wybierz opcję (1-5): ")

        if choice == '1':
            library.display_all_books()
        elif choice == '2':
            new_book = get_book_data()
            if new_book:
                library.add_book(new_book)
        elif choice == '3':
            query = input("Wpisz szukany tytuł lub autora: ")
            results = library.search_books(query)
            if not results.empty:
                print("\n--- Znalezione książki ---")
                print(results.set_index('id').to_string())
                print("------------------------\n")
            else:
                print("Nie znaleziono żadnych książek pasujących do zapytania.")
        elif choice == '4':
            try:
                id_to_remove = int(input("Podaj numeryczne ID książki do usunięcia: "))
                library.remove_book(id_to_remove)
            except ValueError:
                print("Błąd: ID musi być liczbą.")
        elif choice == '5':
            print("Do zobaczenia!")
            break
        else:
            print("Nieprawidłowy wybór. Wybierz opcję od 1 do 5.")


if __name__ == "__main__":
    main()