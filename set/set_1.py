# sample_set={1,2,3,4,5,{9,10}} python cannot contain set within a set

# sample_set={1,2,3,4,5,6,7}
# sample_list=[1,2,3,sample_set]
# sample_tuple=(1,2,3,4,5,sample_set)
# print(sample_set)
# print(sample_list)
# print(sample_tuple)


sam_set={1,2,3,4,5,6,7,8,9}
print(1 in sam_set)
sam_set.add(10)
print(sam_set)
sam_set.update([11,12,13])
print(sam_set)
sam_set.update((14,15,16))
print(sam_set)

sam_set.remove(13)
print(sam_set)
sam_set.pop()
print(sam_set)
print(sam_set.pop())
print(sam_set.pop())
print(sam_set.pop())

set_rough={'false data','malicious data'}
print(set_rough )
del set_rough
# print(set_rough)