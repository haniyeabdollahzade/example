def changename(data):
    
    res = {}
    for k, v in data.items():
        if k == 1:
            res["A"] = v
        elif k == 2:
            res["B"] = v
    return res        

data = {1:10, 2:20}
print(changename(data))
