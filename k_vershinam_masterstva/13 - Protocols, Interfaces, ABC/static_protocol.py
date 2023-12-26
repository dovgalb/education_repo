class Printable:
    def print_info(self) -> None:
        pass


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def print_info(self) -> None:
        print(f"Circle with radius {self.radius}")


class Rectangle:
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def print_info(self) -> None:
        print(f"Rectangle with length {self.length} and width {self.width}")


def print_object_info(obj: Printable) -> None:
    obj.print_info()


circle = Circle(5.0)
rectangle = Rectangle(3.0, 4.0)

print_object_info(circle)
print_object_info(rectangle)

