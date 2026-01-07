from typing import Union
from typing import Optional

def add_list(num_list : list[int]) -> Optional[int]:
	ans=0
	for num in num_list:
		ans+=num
	if ans == 0:
		return None
	return ans

def get_id(id_number : str | int) :
	print(f"User ID {id_number}")

def display(name:str) -> str:
	return f"Displaying the name {name}"

def get_dict(nums: list[int]) -> dict[str,int]:
	return {f"key of {num}" : num for num in nums}

if __name__ == "__main__" :
	print(display("aditya"))
	print(get_dict([1,2,3,4,5,6]))
	print(add_list([1,2,3]))
	print(add_list([]))
	get_id(45)
	get_id("45")
	# print(get_dict(""))

