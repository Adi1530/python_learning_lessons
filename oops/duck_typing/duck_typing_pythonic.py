class Duck:
    def quack(self):
        print("Duck quacks")

    def fly(self):
        print("flies")

class Person:
    def quack(self):
        print("Human quacking")
    def fly(self):
        print("cant fly")

def quack_fly(obj):
    obj.quack()
    obj.fly()


duck=Duck()
quack_fly(duck)

person=Person()
quack_fly(person)
