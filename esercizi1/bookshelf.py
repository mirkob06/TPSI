class Book():

    total_books = 0

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

        Book.total_books += 1

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")

    @staticmethod
    def count_books():
        return f"Total number of books in the library: {Book.total_books}"


book1 = Book("The Lord of the Rings", "J.R.R. Tolkien", "456894")
book2 = Book("Harry Potter", "J.K. Rowling", "5467663")

book1.display_info()
book2.display_info()

print(Book.count_books())
