class Geometric_shapes:
    pass
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
rectangle = Geometric_shapes(x="5", y="10", width="30", height="50")
print("Rectangle", rectangle.x, rectangle.y, rectangle.width, rectangle.height)

class Square:
    def __init__(self, r):
        self.r = r
square = Square(r="2")
print("Square", square.r)

class Parallelogram:
    def __init__(self, a, h):
        self.a = a
        self.h = h
parallelog = Parallelogram(a="", h="")
print("Параллелограмм", parallelog.a, parallelog.h)

class Trapeze:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
trapeze = Trapeze(a="", b="", h="")
print("Трапеция", trapeze.a, trapeze.b, trapeze.h)

class Triangle:
    def __init__(self, a, h):
        self.a = a
        self.h = h
triangle = Triangle(a="", h="")
print("Треугольник", triangle.a, triangle.h)









