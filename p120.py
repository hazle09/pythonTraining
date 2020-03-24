my_list = ["A", "b", "c", "D"]
for i in my_list:
    if i.islower()==True:
        print(i.upper(),end="")
    else:
        print(i.lower(),end="")