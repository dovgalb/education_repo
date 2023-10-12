from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class ILine(ABC):
    @abstractmethod
    def draw_line(self):
        pass


class ICircle(ABC):
    @abstractmethod
    def draw_circle(self):
        pass


class IRectangle(ABC):
    @abstractmethod
    def draw_rect(self):
        pass


class Circle(ICircle):
    def draw_circle(self):
        print('рисование круга')


class Line(ILine):
    def draw_line(self):
        print('рисование линии')


class Rectangle(IRectangle):
    def draw_rect(self):
        print('рисование прямоугольника')


if __name__ == '__main__':
    l = Line()
    print(l.draw_line())