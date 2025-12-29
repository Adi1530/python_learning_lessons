
if __name__=="__main__":
    l=[1,2,3,4,5]
    print(l)
    print("_________________________________________________________________")
    print(dir(l))
    iterator_l=l.__iter__()
    #iterator_l=iter(l)
    print("_________________________________________________________________")
    print(dir(iterator_l))
    print("_________________________________________________________________")
    print(next(iterator_l))
    print(next(iterator_l))
    print(next(iterator_l))