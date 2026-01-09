from typing import Protocol, runtime_checkable

@runtime_checkable
class MyClass(Protocol):
    def say_hi(self):
        print("hiiii")

class Greet:
    def say_hi(self):
        print("hi")

g= Greet()
print(isinstance(g, Greet))