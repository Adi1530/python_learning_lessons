from collections.abc import Sequence
from typing import TypeVar

T = TypeVar('T')
def get_first(collection: Sequence[T]) -> T:
    return collection[0]

people = [1,2,3,4]
print(get_first(people))