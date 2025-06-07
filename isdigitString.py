def isdigitDtring(items):
    item = ''
    for i in items:
        try:
            float(i)
            item += i + ' '
        except ValueError:
            pass   
    return item.strip()     


items = ['127', 'ABC', '12.5', '3D']
print(isdigitDtring(items))