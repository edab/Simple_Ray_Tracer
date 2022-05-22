import math


class Vector:
    """A three element vector used in 3D graphics for multiple purposes"""

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x:0.1f}, {self.y:0.1f}, {self.z:0.1f})"

    def dot_product(self, other):
        """Evaluate the dot product of two vectors"""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def magnitude(self):
        """Evaluate the magnitude of a vector"""
        return math.sqrt(self.dot_product(self))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            raise ValueError("Both operands should be of Vector type.")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x / other.x, self.y / other.y, self.z / other.z)
        else:
            raise ValueError("Both operands should be of Vector type.")
