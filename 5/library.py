class Library:
    def __init__(self, books):
        self.books = books

    def addBook(self, book):
        self.books[book.title] = book

    def rentBook(self, title):
        book.title(title).rent()

    def findBook(self, author):
        try:
            print(self.books[author])
        except:
            print("Nothing")

    def booksAvailable(self):
        temp = []
        for i, j in self.books.items():
            temp.append((i,str(j)))
        return temp

    def __add__(self):
        pass

class Book:
    def __init__(self, title, author, year, available):
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    def __str__(self):
        return f"Title: {self.title} Author: {self.author} Year of release: {self.year} Avaliable: {self.available}"

    def rent(self):
        if books[title].available:
            print("Book "+self.title+" rented")
            books[title].available = False
        else:
            print("Book "+self.title+" not avaliable")
    def returnBook(self):
        if self.available == False:
            self.available = True
        else:
            print("sth wrong")

def filter_by_year(library, y_min, y_max):
    temp = {}
    for i in library.books:
        if i.value.year in range(y_min, y_max):
            # temp[i.value.year] = 
            pass

def main():
    b1 = Book("Hobbit", "Tolkien", 1937, True)
    b2 = Book("Lotr", "Tolkien", 1954, True)
    b3 = Book("Hobbyt", "Jan", 1939, False)
    books = {}
    lib = Library(books)
    lib.addBook(b1)
    lib.addBook(b2)
    lib.addBook(b3)
    print(lib.booksAvailable())
    lib.findBook("Hobbyt")
main()
