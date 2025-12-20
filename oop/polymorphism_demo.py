# polymorphism_demo.py
import math

# Base class
class Shape:
    def area(self):
        """Base method to be overridden by derived classes."""
        raise NotImplementedError("This method should be overridden by subclasses.")

# Derived class for Rectangle
class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of rectangle."""
        return self.length * self.width

# Derived class for Circle
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Calculate area of circle."""
        return math.pi * (self.radius ** 2)
