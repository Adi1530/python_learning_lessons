
class Myclass:
    def __init__(self,func):
        self.func=func
    def __call__(self,*args,**kwargs):
        print("Helloo")
        return self.func(*args,**kwargs)

@Myclass
def say_hi(*args,**kwargs):
    print("hiiiiiii")
say_hi(1,2)