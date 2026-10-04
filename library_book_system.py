# Assignment Information
# Author: Pedro Gonzalez San Martin
# Date: 2026-10-4
# Assignment: Programming Assignment - Student Grade Analyzer
# Tier: Base Level

# Library Book Management System
# This module defines a Book class and demonstrates how library book availability, borrowing, returns, sorting, and filtering work.
class Book:
    """Represents a single library book and its circulation status."""

    def __init__(self, title, author, isbn, year, genre):
        # Store the basic details for each book.
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.genre = genre

        # Track whether the book is currently available to borrow.
        self.available = True
        self.borrower = None

    def get_status(self):
        # Return the current availability status of the book.
        if self.available:
            return "Available"
        return f"Checked out to {self.borrower}"

    def check_out(self, patron_name):
        # If the book is available, mark it as checked out and record the borrower.
        if self.available:
            self.available = False
            self.borrower = patron_name
            return True
        return False

    def return_book(self):
        # Reset the book to its default available state after it is returned.
        self.available = True
        self.borrower = None
        return f"'{self.title}' has been returned and is now available."

    def __str__(self):
        # Format the book details in a readable table-like string.
        return (
            f"{self.isbn:<15} | {self.title:<22} by {self.author:<20} "
            f"({self.year}) [{self.genre:<15}] - {self.get_status()}"
        )


# Starter library collection of six book objects
collection = [
    Book("Dune", "Frank Herbert", "978-0441013593", 1965, "Science Fiction"),
    Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565", 1925, "Classic Fiction"),
    Book("Educated", "Tara Westover", "978-0399590504", 2018, "Memoir"),
    Book("1984", "George Orwell", "978-0451524935", 1949, "Dystopian"),
    Book("To Kill a Mockingbird", "Harper Lee", "978-0060935467", 1960, "Classic Fiction"),
    Book("The Hobbit", "J.R.R. Tolkien", "978-0547928227", 1937, "Fantasy"),
]

# Display the full collection before any transactions
print("=== Full Collection ===")
for book in collection:
    print(book)

# Simulate borrowing and returning books
print("\n=== Checkout Operations ===")
if collection[0].check_out("Jordan"):
    print(f"'{collection[0].title}' checked out to Jordan.")
else:
    print(f"'{collection[0].title}' is already checked out.")

if collection[1].check_out("Priya"):
    print(f"'{collection[1].title}' checked out to Priya.")
else:
    print(f"'{collection[1].title}' is already checked out.")

if collection[0].check_out("Alex"):
    print(f"'{collection[0].title}' checked out to Alex.")
else:
    print(f"'{collection[0].title}' is already checked out.")

return_message = collection[1].return_book()
print(return_message)

# Sort books alphabetically by title without changing the original collection
print("\n=== Books Sorted by Title ===")
sorted_by_title = sorted(collection, key=lambda b: b.title)
for book in sorted_by_title:
    print(book)

# Show only the books currently available for checkout
print("\n=== Available Books ===")
available_books = [book for book in collection if book.available]
for book in available_books:
    print(book)
