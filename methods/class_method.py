


class MyClass:
    count=0
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        MyClass.count+=1

    @classmethod
    def get_user_count(cls):
        return cls.count


    def display_info(self):
        print(f"Name : {self.name} | Age : {self.age} | Gender : {self.gender}")

myclass=MyClass("Aditya",20,"M")
myclass_=MyClass("Aditya",20,"M")
myclass.display_info()
print(myclass.get_user_count())
print(MyClass.get_user_count())
