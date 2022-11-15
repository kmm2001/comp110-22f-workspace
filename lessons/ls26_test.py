
from __future__ import annotations 

class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Contruct."""
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """Str."""
        return f"{self.x}, {self.y}"

    def scale(self, factor: float) -> Point:
        """Scale point."""
        return Point(self.x * factor, self.y * factor)

    def __mul__(self, factor: float) -> Point:
        """Multiply."""
        return Point(self.x * factor, self.y * factor)

a: Point = Point(1.0, 2.0)
b: Point = a * 2
print(a)
print(b)