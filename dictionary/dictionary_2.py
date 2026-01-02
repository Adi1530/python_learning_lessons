# sample={'a':1,'b':2,'c':3,'d':4,'e':5}
#
# sample_={'f':6}
# final_dict=sample | sample_
#
# print(final_dict)

#
# def dump_dict(**kwargs):
#     return kwargs
#
# print(dump_dict(**{'a':1,'b':2} , c=3 , **{'d':4}))

dict_1={'a':1}
dict_2={'b':2}
merged={**dict_1 , **dict_2}
print(merged)

import collections