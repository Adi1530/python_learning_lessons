
def dict_check(sample):
    try:
        print(f"{sample['name']}  |  {sample['age']}  |  {sample['Gender']}")

    except KeyError as e:
        print(f"Missing keys {e}")

if __name__ == "__main__":
    sample_one={"name":"aditya","age":20,"Gender":"M"}
    sample_two = {"name": "aditya", "Gender": "M"}

    dict_check(sample_one)
    dict_check(sample_two)



