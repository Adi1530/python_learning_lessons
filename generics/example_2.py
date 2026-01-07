from typing import TypeVar

K = TypeVar('K')
V = TypeVar('V')

def get_value(dict_input : dict[K,V] , user_key : K) -> V :
    return dict_input[user_key]

users: dict[int,str] = {1 : "adi" , 2 : "hari"}
print(get_value(users , 1))