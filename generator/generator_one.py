def nums_generator():
	for i in range(10):
		yield i

if __name__=="__main__":
	nums=nums_generator()
	#print(next(nums))
	#print(next(nums))

	for num in nums:
		print(num)