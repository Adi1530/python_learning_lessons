if __name__ == "__main__" :
    sample_list=[('aditya',22),('tom',23),('ram',24),('kisore',51),('pranav',75),('kavin',73)]

    sample_dict = {name:roll for name,roll in sample_list}

    print("In this name is the key")
    print(sample_dict)
    print(dir(sample_dict))

    print("In this roll is the key")
    sample_dict = {roll: name for name, roll in sample_list}
    print(sample_dict)

    sorted_dict= {name : roll for name, roll in sorted(sample_dict.items())}
    print(sorted_dict)