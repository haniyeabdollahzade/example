def fruits(tuple_of_fruit):
    good = {}

    for friut in tuple_of_fruit:
        name = friut['name']
        shape = friut['shape']
        mass = friut['mass']
        volume = friut['volume']

        if shape == 'sphere' and 300 <= mass <= 600 and 100 <= volume <= 500:
            if name in good:
                good[name] += 1
            else:
                good[name] = 1
    return good            


output = fruits ((
    {'name':'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
    {'name':'mango', 'shape': 'square', 'mass': 150, 'volume': 120}, 
    {'name':'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
    {'name':'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250}))

print(output)