from dataclasses import dataclass


@dataclass
class Rectangle:
    width: int
    high: int

    def get_pr(self):
        return 2 * (self.width + self.high)


@dataclass
class Square:
    side: int

    def get_pr(self):
        return 4 * self.side


@dataclass
class Triangle:
    a: int
    b: int
    c: int

    def get_pr(self):
        return self.a + self.b + self.c


if __name__ == "__main__":
    r1 = Rectangle(1, 2)
    r2 = Rectangle(3, 4)
    s1 = Square(10)
    s2 = Square(20)
    t1 = Triangle(1,2,3)
    t2 = Triangle(5,2,9)

    geom = [r1, r2, s1, s2, t1, t2]

    for g in geom:
        print(g.get_pr())
