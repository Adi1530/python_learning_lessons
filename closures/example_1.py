def multiply_operation(n):
	def multiple_with(x):
		return x*n
	return multiple_with

double = multiply_operation(2)
triple=multiply_operation(3)

print(double(5))

print(triple(6))
print(double.__closure__)
print(double.__closure__[0].cell_contents)