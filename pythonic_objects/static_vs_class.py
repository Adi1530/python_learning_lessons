class MyClass:
	@classmethod
	def class_m(*args): #we have to pass the class itself as the first arg
		return args
	@staticmethod
	def class_s(*args):
		return args
	
myclass=MyClass()
print(MyClass.class_m())
print(MyClass.class_s())

