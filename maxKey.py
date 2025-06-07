def maxkey(data):
    max_key = []
    max_value = max(data.values())
    for key, val in data.items():
        if val == max_value:
            max_key.append(key)
    return max_key

data = {"A": 2, "B": 7, "C":3, "D": 7}
print(maxkey(data))        
