def square_the_list(func,list_input):
	result=[]
	for i in list_input:
		result.append(func(i))
	return result

def square(num):
	return num*num

if __name__ == "__main__":
	nums=[1,2,3,4,5,6,7,8,9]
	a=square
	ans=square_the_list(a,nums)
	print(ans)
