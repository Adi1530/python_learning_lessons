from typing import TypedDict

class User(TypedDict):
    name : str
    id : int

def create_user() -> User:
    user : User ={
        "name" : input("Enter name :"),
        "id" : int(input("Enter id"))
    }
    return user

if __name__ == "__main__":
    users : list[User] = []
    while(True):

        users.append(create_user())
        flag = int(input("0 -- > Exit | 1 --> Add Another user | 2--> Display user db"))
        if flag == 0 :
            break
        if flag == 1:
            continue
        if flag == 2:
            for user in users:
                print(user)




#
# Enter name :aditya
# Enter id8096
# 0 -- > Exit | 1 --> Add Another user | 2--> Display user db1
# Enter name :swetha
# Enter id3456
# 0 -- > Exit | 1 --> Add Another user | 2--> Display user db1
# Enter name :kavin`
# Enter id543
# 0 -- > Exit | 1 --> Add Another user | 2--> Display user db1
# Enter name :kisore
# Enter id7890
# 0 -- > Exit | 1 --> Add Another user | 2--> Display user db2
# {'name': 'aditya', 'id': 8096}
# {'name': 'swetha', 'id': 3456}
# {'name': 'kavin', 'id': 543}
# {'name': 'kisore', 'id': 7890}
# Enter name :