import math

class Shape:
    def area(self):
        """Base method that should be overridden in subclasses."""
        raise NotImplementedError("Subclasses must override the area() method")


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of rectangle."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Calculate area of circle."""
        return math.pi * (self.radius ** 2)
