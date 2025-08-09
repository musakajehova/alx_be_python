import math
class Shape:

    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def area(self):
        total_area = self.length * self.width
        return total_area

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def area(self):
        total_area = math.pi * self.radius** 2
        return total_area