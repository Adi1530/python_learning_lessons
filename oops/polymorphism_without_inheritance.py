#achieved by using duck typing


class GroundFloor:
    def is_pista_available(self):
        print("yes")
class FirstFloor:
    def is_pista_available(self):
        print("yes")
class SecondFloor:
    def is_pista_available(self):
        print("no")
class ThirdFloor:
    def is_pista_available(self):
        print("no")

def check_pantry(obj):
    obj.is_pista_available()

if __name__ == "__main__":
    ground_floor=GroundFloor()
    first_floor=FirstFloor()
    second_floor=SecondFloor()
    third_floor=ThirdFloor()

    obj_list=[ground_floor,first_floor,second_floor,third_floor]

    for obj in obj_list:
        check_pantry(obj)
