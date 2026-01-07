import decorator
def decorating_function(original_function):
	print("Decorating function")
	return original_function

@decorating_function
def decorated():
	pass

decorated()


