import math
class Shape:

    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, lenth, width):
        super().__init__()
        self.lenth = lenth
        self.width = width
    
    def area(self):
        total_area = self.lenth*self.width
        return total_area

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def area(self):
        total_area = math.pi * self.radius**2
        return total_area