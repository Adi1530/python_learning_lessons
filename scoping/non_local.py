def counter():
    count=0
    def incrementer():
        nonlocal count
        count+=1
        print("+1 done")
        print(count)
    print(count)
    return incrementer()


counter()

#
# def counter():
#     count=0
#     def count_add():
#         nonlocal count
#         count=10
#         return count
#     print(count_add())
#     print(count)
#
# if __name__ == "__main__" :
#     counter()