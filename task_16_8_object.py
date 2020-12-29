from task_16_8_class import Rectangle, Square, Circle

rec1 = Rectangle(3, 4)
rec2 = Rectangle(12, 5)
square1 = Square(5)
square2 = Square(10)
i = 0
circle1 = Circle(66)
circle2 = Circle(83)

print(f"Rectangle 1 area = {rec1.get_area_rectangle()}")
print(f"Rectangle 2 area = {rec2.get_area_rectangle()}")
print(f"Square 1 area = {square1.get_area_square()}")
print(f"Square 2 area = {square2.get_area_square()}")
print(f"Circle 1 area = %0.2f" % circle1.get_area_circle())
print(f"Circle 2 area = %0.2f" % circle2.get_area_circle())
print()

figures = [rec1, square1, rec2, square2, i, circle1, circle2]

ri = 0
si = 0
ci = 0
for fig in figures:
    if isinstance(fig, Rectangle):
        ri += 1
        print(fig.name, ri, "area =", fig.get_area_rectangle())
    elif isinstance(fig, Square):
        si += 1
        print(fig.name, si, "area =", fig.get_area_square())
    elif isinstance(fig, Circle):
        ci+= 1
        print(fig.name, ci, "area = %0.2f" % fig.get_area_circle())
    else:
        print("Unknown figure")
