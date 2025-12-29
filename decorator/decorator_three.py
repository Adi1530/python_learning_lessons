def decorator_f(function_arg):
	def wrapper_f(*args,**kwargs):
		print("arbitrary number of positional arguement consuming wrapper function executed")
		return function_arg(*args,**kwargs)
	return wrapper_f

@decorator_f
def display():
	print("HI")

@decorator_f
def display_list(nums):
	for num in nums:
		print(num)

display()
display_list([1,2,3,4,5])
