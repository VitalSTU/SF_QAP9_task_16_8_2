import math


class Rectangle:
    def __init__(self, a, b):
        self.name = "Rectangle"
        self.a = a
        self.b = b

    def get_area_rectangle(self):
        return self.a * self.b


class Square:
    def __init__(self, a):
        self.name = "Square"
        self.a = a

    def get_area_square(self):
        return self.a ** 2


class Circle:
    def __init__(self, r):
        self.name = "Circle"
        self.r = r

    def get_area_circle(self):
        return math.pi * self.r ** 2
