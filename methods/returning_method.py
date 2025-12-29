def outer_func():
	print("Hey the inner function whats the value?")
	def inner_func():
		a=5
		print("The value is {a}")
	return inner_func()
if __name__ == "__main__":
	outer_func()
