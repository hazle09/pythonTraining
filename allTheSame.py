def all_the_same(lst):
    for j in range(len(lst)):
        if lst[j+1]!=lst[j]:
            return False
        elif not lst:
            return True
        else:
            return True

print(all_the_same([]))

# lll=[1,2,3]

# print(lll[0]==lll[1])

# for i in lll:
#     print()

