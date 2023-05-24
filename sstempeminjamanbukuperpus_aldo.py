class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
    
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nAvailability: {'Available' if self.is_available else 'Not Available'}"

class LibraryMember:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed the book: {book.title}")
        else:
            print(f"The book {book.title} is not available for borrowing.")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned the book: {book.title}")
        else:
            print(f"{self.name} did not borrow the book: {book.title}")
    
    def display_borrowed_books(self):
        print(f"{self.name}'s borrowed books:")
        if len(self.borrowed_books) == 0:
            print("No books borrowed.")
        else:
            for book in self.borrowed_books:
                print(book)
                print("")

# Membuat objek LibraryMember
member1 = LibraryMember("John Doe")

# Membuat objek Book
book1 = Book("Book 1", "Author 1")
book2 = Book("Book 2", "Author 2")
book3 = Book("Book 3", "Author 3")

# Meminjam buku
member1.borrow_book(book1)
member1.borrow_book(book2)

# Menampilkan daftar buku yang dipinjam
member1.display_borrowed_books()

# Mengembalikan buku
member1.return_book(book1)

# Menampilkan daftar buku yang dipinjam setelah pengembalian
member1.display_borrowed_books()