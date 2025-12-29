def outer_func(country):
	def inner_func(state):
		print(f"Country - {country} | State - {state}")

	return inner_func

if __name__ == "__main__":
	f=outer_func("India")
	f("Tamil Nadu")
