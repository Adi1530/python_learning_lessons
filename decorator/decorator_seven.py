from functools import singledispatch

from typing import Any

@singledispatch
def func(arg : Any):
    # print(arg)
    raise NotImplemented

@func.register
def _(arg : int, verbose = False):
    if verbose :
        print("Heres your integer : ",arg)
        return
    print(arg)


@func.register
def _(arg : str, verbose = False):
    if verbose :
        print("Heres your string : ",arg)
        return
    print(arg)


if __name__ == '__main__':
    func(1,True)
    func("adi")
    func("adi",True)
    # func([])

