# library_system.py

# Base class
class Book:
    def __init__(self, title: _str_, author: _str_):
        self.title = title
        self.author = author

# Derived class for ebooks
class EBook(Book):
    def __init__(self, title: _str_, author: _str_, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

# Derived class for print books
class PrintBook(Book):
    def __init__(self, title: _str_, author: _str_, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

# Library class demonstrating composition
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        """Add a book instance to the library."""
        self.books.append(book)

    def list_books(self):
        """List all books with details based on their type."""
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")
