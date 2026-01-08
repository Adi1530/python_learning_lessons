
class MyClass:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __bool__(self):
		return bool(self.x or self.y)

myclass = MyClass(0,0)
position = MyClass(0,1)
print(bool(myclass))
print(bool(position))
