names = ['Ali Cheraghi', 'Romina Bayat', 'Hessam Akbari', 'Maryam Darabi']

sort_list = []
for i in names:
    name = tuple(i.split(' '))
    sort_list.append(name)

sorted_list = sorted(sort_list, key=lambda i :i[1])
for i in sorted_list:
    print(i[0], i[1])
