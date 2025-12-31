
def dict_check(sample):
    if "name" in sample and "age" in sample and "Gender" in sample:
        print("Valid dict ")
    else:
        print("Invalid dict")

if __name__ == "__main__":
    sample_one={"name":"aditya","age":20,"Gender":"M"}
    sample_two = {"name": "aditya", "Gender": "M"}

    dict_check(sample_one)
    dict_check(sample_two)



