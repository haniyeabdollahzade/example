PI = 3.14159
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return PI * self.radius**2

    def calc_circumference(self):
        return 2 * PI * self.radius

    def __str__(self):
        return f"A circle with a radius of {self.radius}."
    

C = Circle(2)
print(C.calc_area())
print(C.calc_circumference())  