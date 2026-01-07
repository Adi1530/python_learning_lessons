from typing import cast, Any, get_type_hints

def parse(num : Any) -> float:
    # x=float(num)
    # return x

    return cast(float,float(num))
#     the cast line is only to tell static type checkers that this is a float val no impact on code at all
if __name__ == "__main__":
    print(parse(10))
    print(get_type_hints(parse))