from collections import UserDict

class MyClass(UserDict):
    def __getitem__(self , key):
        print("Using super Keyword")
        return super().__getitem__(key)

myclass=MyClass({"7":"C" , "6":"D"})
print(myclass)