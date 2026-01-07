import functools
import random

def magic_pot(original_function):
	@functools.wraps(original_function)
	def wrapper_fun():
		l=["car","bike","laptop","graphics card"]
		print(random.choice(l))
		return original_function()
	return wrapper_fun

@magic_pot
def magic():
	print("Abraka Dahbhraaa")

magic()
print(magic.__name__)