from typing import Protocol

class Writeable(Protocol):
    def write(self):
        """to write something"""



class Readable(Protocol):
    def read(self):
        """to read something"""

def write_stuff(writeable : Writeable):
    return writeable.write()
def read_stuff(readable : Readable):
    return readable.read()

class Author:
    def __init__(self,name,book):
        self.name = name
        self.book = book

    def write(self):
        print(f"Author, {self.name} is writing {self.book}")

    def read(self):
        print(f"Author, {self.name} is reading {self.book}")


author = Author("Aditya","python")
write_stuff(author)
read_stuff(author)