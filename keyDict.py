def keyDict(dic):
    keyfreq = {}

    for i in dic:
        for key in i.keys():
            if key in keyfreq:
                keyfreq[key] += 1
            else:
                keyfreq[key] = 1

    key = list(keyfreq)
    return key
       

                

dic = [
    {'a':1, 'b':2},
    {'b':3, 'c':4},
    {'d': 5, 'a':6}
]
print(keyDict(dic))

