from typing import Protocol

class Printable(Protocol):
    pages : int
    def print_item(self):
        pass

    def recycle(self):
        pass


class Book:
    pages : int

    def __init__(self, name):
        self.name=name

    def print_item(self):
        print(f"This is a book named {self.name}")

    def recycle(self):
        print(f"Recycling {self.name}")

    def say_title(self):
        print("The title of the book : ",self.name)

def print_printable(printable : Printable):
    printable.print_item()

book = Book("python")
# book_2 : Printable = Book("java")

book.print_item()
print_printable(book)