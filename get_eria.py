import math

def square_area(side):
    return side * side

def circle_area(radius):
    return math.pi * radius ** 2

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return (base * height) / 2

def get_func(ls):
    func_list = []
    for shape in ls:
        if shape == 'square':
            func_list.append(square_area)
        elif shape == 'circle':
            func_list.append(circle_area)
        elif shape == 'rectangle':
            func_list.append(rectangle_area)
        elif shape == 'triangle':
            func_list.append(triangle_area)

    return func_list

ls = get_func(['square', 'circle', 'rectangle', 'triangle'])

print(ls[0](1))     
print(ls[1](2))      
print(ls[2](2, 4))   
print(ls[3](4, 5))   
