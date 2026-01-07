def repeat(n):
    def decorating_fun(func):
        def wrapper():
            for i in range(n):
                func()
            return None
        return wrapper
    return decorating_fun


@repeat(5)
def greet():
    print("hello")

greet()