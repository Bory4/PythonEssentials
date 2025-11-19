class Publication:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def description(self):
        return f"Publication - Title: {self.title}; Author: {self.author}; Year: {self.year}"

class Book(Publication):
    def description(self):
        return f"Book - Title: {self.title}; Author: {self.author}; Year: {self.year}"
    
class Ebook(Book):
    def __init__(self, title, author, year, filetype):
        super().__init__(title, author, year)
        self.filetype = filetype

    def description(self):
        filetype = super().description()
        return f"Ebook - Title: {self.title}; Author: {self.author}; Year: {self.year}, Filetype: {self.filetype}"

def show_description(cla):
    print(cla.description())

aaa = Publication("Adam", "PTSD", 1984)
bbb = Book("Bar","bar",1999)
ccc = Ebook("Coin","Sadam",2024,"PDF")

show_description(aaa)
show_description(bbb)
show_description(ccc)
