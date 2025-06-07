mylist = [1, 2, 2, 4, 1, 3, 3, 3, 6]

rep_list  = []
for i in set(mylist):
    if mylist.count(i) > 1:
        rep_list.append(i)

print(rep_list)