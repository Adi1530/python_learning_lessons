if __name__ == "__main__":


    def sum_num(*args):
        # """sum_num method documentation"""
        ans=0
        for arg in args:
            ans+=arg
        print(ans)


    sum_num(4, 3, 2)
    print(sum_num.__doc__)