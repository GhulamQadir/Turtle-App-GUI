class Point:
    def __init__(self, x, y):
        # Private attributes (cannot be accessed directly from outside the class)
        self.__x = x
        self.__y = y

    # Getter for x: allows reading the value like point.x
    @property
    def x(self):
        return self.__x

    # Setter for x: allows updating the value like point.x = 10
    @x.setter
    def x(self, updated_x: float):
        self.__x = updated_x

    # Getter for y: allows reading the value like point.y
    @property
    def y(self):
        return self.__y

    # Setter for y: allows updating the value like point.y = 20
    @y.setter
    def y(self, updated_y: float):
        self.__y = updated_y

    # Add two Point objects using the + operator
    # Example: p3 = p1 + p2
    def __add__(self, other_point):
        x = self.__x + other_point.__x
        y = self.__y + other_point.__y
        return Point(x, y)

    # Subtract two Point objects using the - operator
    # Example: p3 = p1 - p2
    def __sub__(self, other_point):
        x = self.__x - other_point.__x
        y = self.__y - other_point.__y
        return Point(x, y)

    # String representation of the object when printed
    # Example: print(p) → P(3, 4)
    def __str__(self):
        return f"P({self.__x}, {self.__y})"
