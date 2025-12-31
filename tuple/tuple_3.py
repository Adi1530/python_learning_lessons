from collections import namedtuple

city=namedtuple('city',['name','state','country'])

city_one=city('trichy','Tamil Nadu','India')
city_two=city('madurai','madurai','India')
city_three=city('chennai','Tamil Nadu','India')

print(city_one.name)
print(city_three.state)
print(city_two.country)
print(isinstance(city_one,city))
print(city_two)
print(dir(city_two))
city_two_iterable_tuple=iter(city_two)
print(dir(city_two_iterable_tuple))
print(next(city_two_iterable_tuple))
print(next(city_two_iterable_tuple))

x=('adi','tom','tom',)
print(x)


#Food=namedtuple('Food',['main_course','main_course','printit'])
#print(Food)
# you cant have duplicate fieldnames and invalid identifiers and keywords as field names in named tuple

Food=namedtuple('Food',['main_course','side','printit'],rename=True)
food=Food('idly','sambar','egg')

print(food)