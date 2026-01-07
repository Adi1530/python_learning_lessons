from typing import TypeVar , Generic

T = TypeVar('T')

class ListDemo(Generic[T]):
    def __init__(self,items : list[T]) -> None :
        self.items = items

    def list_append(self,item : T):
        self.items.append(item)

    def display_list(self):
        for item in self.items:
            print(item)

    def list_remove(self , item : T):
        if item in self.items:
            self.items.remove(item)

if __name__ == "__main__" :
    ld = ListDemo([1,2,3,4,5,6])
    lds = ListDemo(["adi","hari"])
    ld.display_list()
    lds.display_list()
    lds.list_append(1)
