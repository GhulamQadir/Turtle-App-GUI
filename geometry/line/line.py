from geometry.point.point import Point


class Line:
    # Constructor: creates a Line object using two Point objects
    def __init__(self, start_point: Point, end_point: Point):
        # Private attributes (encapsulation)
        # start_point and end_point are both instances of Point
        self.__start_point = start_point
        self.__end_point = end_point

    # Getter for start_point
    @property
    def start_point(self):
        return self.__start_point

    # Setter for start_point
    @start_point.setter
    def start_point(self, updated_point: Point):
        self.__start_point = updated_point

    # Getter for end_point
    @property
    def end_point(self):
        return self.__end_point

    # Setter for end_point
    @end_point.setter
    def end_point(self, updated_point: Point):
        self.__end_point = updated_point

    # String representation of the Line object
    # Example: print(line) → Line from P(0, 0) to P(3, 4)
    def __str__(self):
        return f"Line from P({self.__start_point.x}, {self.__start_point.y}) to P({self.__end_point.x}, {self.__end_point.y})"
