from collections import defaultdict

# sample_dict=defaultdict()
#
# sample_dict=[]
# print(sample_dict[0])


sample_dict=defaultdict(list)
#
#
# sample_list=["aditya","ram","tom","kavin"]
#
# for k in sample_list:
#     print(sample_dict[k])
#

sample_dict['laliga'].append("Real Madrid")
sample_dict['epl'].append("Manchester United")
sample_dict['laliga'].append("Atletico Madrid")
print(dict(sample_dict))

dict_one={'a':[1,2,3]}
print(dict_one)
dict_one['a'].append(1)
print(dict_one)