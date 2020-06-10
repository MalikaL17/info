# Модуль с классом, задающим прямоугольник и методы для поиска его периметра и площади
class Rectangle(object):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def area(self):
        return self.width * self.length


if __name__ == "__main__":
    rectangle = Rectangle(width=5, length=3)
    print(rectangle.perimeter())
    print(rectangle.area())