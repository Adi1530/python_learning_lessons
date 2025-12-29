def decorator_method(function_argument):
    def wrapper_method():
        print("Wrapper is executed . you can add additional code of the original function here")
        return function_argument()
    return wrapper_method

@decorator_method
def original_function():
    print("This is the line from the original function")


original_function()

