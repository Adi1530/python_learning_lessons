from functools import reduce
from operator import add

print(reduce(add, range(10)))

print(sum(range(10)))

