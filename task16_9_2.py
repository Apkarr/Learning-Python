class Rectangle_a():
    def __init__(self, l, h):
        self.l = l
        self.h = h
        print('Длина=', self.l)
        print('Высота=', self.h)
    def rect_Area(self):
        return self.l * self.h
    def rect_Perimeter(self):
        return 2 * (self.l + self.h)
Rectangle_b = Rectangle_a(10, 5)
print("Площадь", Rectangle_b.rect_Area())
print("Периметр", Rectangle_b.rect_Perimeter())


