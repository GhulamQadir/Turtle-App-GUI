from geometry.point.point import Point
from geometry.line.line import Line


class Pen:
    def __init__(self, canvas):
        # The pen starts at an initial position (25, 100)
        self.__current_pos = Point(25, 100)

        # Canvas object (responsible for actual drawing)
        self.canvas = canvas

    # Getter for current position
    @property
    def current_pos(self):
        return self.__current_pos

    # Setter for current position
    @current_pos.setter
    def current_pos(self, updated_pos):
        self.__current_pos = updated_pos

    # Move the pen to a new position WITHOUT drawing a line
    def move_to(self, x, y):
        self.__current_pos = Point(x, y)

    # Draw a line from the current position to end_point
    def line_to(self, x, y):
        # Create a new Point object using the given (x, y) coordinates
        end_point = Point(x, y)

        # Create a Line object from current position to end_point
        line = Line(self.__current_pos, end_point)

        # Ask the canvas to actually render this line
        self.canvas.add_line(line)

        # Update pen's current position to the new point
        self.current_pos = end_point
