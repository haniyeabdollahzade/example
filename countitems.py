def countitems(items):
    count = {}
    for i in items:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count


items = ["A", "B", "A", "C", "A", "C", "B"]
print(countitems(items))