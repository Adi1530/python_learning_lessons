from typing import overload, Sequence, TypeVar

T = TypeVar('T')

@overload
def maximum(values : Sequence[T]) -> T : ...

@overload
def maximum(a : T , b : T) -> T : ...

def maximum(arg1, arg2 = None):
	if arg2 is None:	
		return max(arg1)
	return arg1 if arg1>=arg2 else arg2


print(maximum([1,2,3,4,5]))
print(maximum(1,2))
