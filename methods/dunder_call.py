import random

class CardGame:
    def __init__(self , items):
        self._items = items
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError as e:
            print(e)


    def __call__(self):
        return self.pick()


if __name__ == "__main__" :
    cardgame=CardGame([1,2,3,4,5,6])
    print(cardgame())
    print(callable(cardgame))
