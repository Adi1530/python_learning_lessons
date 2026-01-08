class MyClass:
    """this is documentation of myclass"""
    x=10
    def documentation(self):
        """hi from documentation"""
        pass
    def __repr__(self):
        '''hi'''
        return f"MyClass()"

    def __str__(self):
        return f"my class object"
myclass = MyClass()
print(myclass.x)

print(str(myclass))
print(repr(myclass))
print(myclass.__str__())
print(myclass.__repr__())

print(myclass.__doc__)
print(myclass.__repr__.__doc__)
print(myclass.documentation.__doc__)
