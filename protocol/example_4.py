from typing import Protocol

class WriteContent(Protocol):
    def write_title(self,title): ...

def write_content(content : WriteContent, title):
    content.write_title(title)

class NewsPaper:
    def __init__(self, name):
        self.name =name
    def write_title(self,title_arg):
        print(f"{title_arg} Authored by {self.name}")

if __name__ == '__main__':
    toi = NewsPaper("Jaiswal")
    write_content(NewsPaper("Aditya"),"personal blog")
