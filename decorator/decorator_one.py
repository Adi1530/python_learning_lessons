def car(original_function):
	print("Car has engine, AC, brakes, hand brake")
	def drive_wrapper():
		print("Drive function executed")
		return original_function()
	return drive_wrapper

def drive():
	print("Only enough to know clutch , accelerator, brakes")



decorated_function=car(drive)
decorated_function()
