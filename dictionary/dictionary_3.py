from typing import TypedDict

class Movie(TypedDict) :
	name : str
	rating : float
	year : int

jaibhim : Movie =  {"name" : "Jaibhim" , "rating" : 9.9 , "year" : 2020}
print(jaibhim)
print(type(jaibhim))
print(dir(jaibhim))
iterable_dict=iter(jaibhim)
print(next(iterable_dict))
print(next(iterable_dict))
# print(jaibhim.)