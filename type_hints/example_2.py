def concat(*args : int , **kwargs : str):
    return f"{args} and {kwargs}"

def keyword_args(*,num_1 : int ,num_2 : int):
    print(f"Keyword arguments are {num_1} and {num_2}")

if __name__ == "__main__":
    print(concat(1,2,4,3,4,5,6,7,5,x="it",t="was"))
    keyword_args(num_1=10,num_2=2)