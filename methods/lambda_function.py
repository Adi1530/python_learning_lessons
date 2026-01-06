# add = lambda a,b : a+b
# print(add(1,2))


nums = [1,2,3,4,5,6,7]

square = map(lambda x : x*x , nums)
print(list(square))

max_num = lambda a,b : a if a > b else b
print(max_num(1000,1))