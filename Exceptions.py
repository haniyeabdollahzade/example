PI = 3.14

def get_number():
    try:
        number = float(input("Please enter a number: "))
        return number
    except ValueError:
        return "You can only enter numbers here."

def calculate_circle_area(radius):

    if radius < 0:
        raise ValueError("The radius must be positive.")
    return PI * radius * radius



        
