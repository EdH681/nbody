import math


class Vector2:
    def __init__(self, *args: float):
        """
        A 2D vector\n
        Enter values in the order (x, y)\n
        """
        self.__x = args[0]
        self.__y = args[1]

    def __str__(self):
        return f"{(self.__x, self.__y)}"

    def __getitem__(self, item):
        if item == "x" or item == 0:
            return self.__x
        elif item == "y" or item == 1:
            return self.__y
        else:
            return None

    def __add__(self, other):
        if isinstance(other, Vector2) or isinstance(other, tuple):
            x = other[0] + self.__x
            y = other[1] + self.__y
            return Vector2(x, y)
        else:
            raise TypeError("Cannot add a vector value to a non-vector value")

    def __radd__(self, other):
        if isinstance(other, Vector2) or isinstance(other, tuple):
            x = other[0] + self.__x
            y = other[1] + self.__y
            return Vector2(x, y)
        else:
            raise TypeError("Cannot add a vector value to a non-vector value")

    def __sub__(self, other):
        if isinstance(other, Vector2) or isinstance(other, tuple):
            x = self.__x - other[0]
            y = self.__y - other[1]
            return Vector2(x, y)
        else:
            raise TypeError("Cannot add a vector value to a non-vector value")

    def __rsub__(self, other):
        if isinstance(other, Vector2) or isinstance(other, tuple):
            x = other[0] - self.__x
            y = other[1] - self.__y
            return Vector2(x, y)
        else:
            raise TypeError("Cannot add a vector value to a non-vector value")

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            x = other * self.__x
            y = other * self.__y
            return x, y
        else:
            raise ValueError("Can only multiply a vector by a scalar")

    def magnitude(self) -> float:
        """
        :return: The magnitude of the vector
        """
        return math.sqrt(self.__x ** 2 + self.__y ** 2)

    def unit(self):
        mag = self.magnitude()
        x = self.__x / mag
        y = self.__y / mag
        return Vector2(x, y)


def dot(a: Vector2, b: Vector2) -> float:
    """
    :param a: Vector A
    :param b: Vector B
    :return: The dot product of A and B
    """
    x = a[0] * b[0]
    y = a[1] * b[1]
    return x+y


def angle(a: Vector2, b: Vector2, deg=False) -> float:
    """
    :param a: Vector A
    :param b: Vector B
    :param deg: Boolean for if degrees are returned, radians if False
    :return: The angle between A and B
    """
    cosTheta = dot(a, b)/(a.magnitude() * b.magnitude())
    theta = math.acos(cosTheta)
    if deg:
        return math.degrees(theta)
    else:
        return theta


def blank():
    """
    Creates an empty vector (0, 0)
    """
    return Vector2(0, 0)


if __name__ == "__main__":
    v1 = Vector2(4, 3)