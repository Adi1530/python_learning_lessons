nums=[1,2,3,4,5,6]

iterator_nums=iter(nums)
while True:
    try:
        print(next(iterator_nums))
    except StopIteration:
        print("Stop Iteration exception run")
        break