from geometry.point.point import Point
from geometry.pen.pen import Pen


class Turtle:
    # --- Movement configuration (class-level constants) ---

    # Number of pixels the turtle moves in one step (fixed for all turtles).
    STEP = 20

    # Minimum space (in pixels) to keep from the top edge of the canvas.
    # This ensures the turtle never overlaps with the top "Clear" button area.
    TOP_MARGIN = 15

    # Minimum space (in pixels) to keep from the left, right, and bottom edges
    # of the canvas so the turtle does not draw outside the visible area.
    EDGE_MARGIN = 5

    # Note: These are defined as **class-level constants** (not instance variables)
    # because they are fixed rules that apply to *all* turtles equally.
    # They don’t depend on any specific turtle or canvas instance,
    # so we avoid storing them in __init__.
    def __init__(self, canvas):
        # Turtle uses a Pen to actually draw on the canvas
        self.pen = Pen(canvas)

        # Get canvas dimensions from Tkinter
        self.window_height = int(canvas.cget("height"))
        self.window_width = int(canvas.cget("width"))

    # Getter for current position of the turtle (delegated to Pen)
    @property
    def current_position(self):
        return self.pen.current_pos

    # Move UP by STEP.
    # Allow the move only if AFTER moving up we will still be >= TOP_MARGIN from the top.
    # That means: current_y >= TOP_MARGIN + STEP  (e.g., 15 + 20 = 35 → y > 34)
    def forward(self):
        if self.current_position.y >= (self.TOP_MARGIN + self.STEP):
            self.pen.line_to(
                self.current_position.x, self.current_position.y - self.STEP
            )

    # Move DOWN by STEP.
    # Allow the move only if AFTER moving down we will still be <= (height - EDGE_MARGIN) from the bottom.
    # That means: current_y <= window_height - EDGE_MARGIN - STEP
    # Example: height - 5 - 20 = height - 25 → check like y < (height - 24)
    def backward(self):
        if self.current_position.y <= (
            self.window_height - self.EDGE_MARGIN - self.STEP
        ):
            self.pen.line_to(
                self.current_position.x, self.current_position.y + self.STEP
            )

    # Move LEFT by STEP.
    # Allow the move only if AFTER moving left we will still be >= EDGE_MARGIN from the left edge.
    # That means: current_x >= EDGE_MARGIN + STEP  (5 + 20 = 25 → x > 24)
    def left(self):
        if self.current_position.x >= (self.EDGE_MARGIN + self.STEP):
            self.pen.line_to(
                self.current_position.x - self.STEP, self.current_position.y
            )

    # Move RIGHT by STEP.
    # Allow the move only if AFTER moving right we will still be <= (width - EDGE_MARGIN) from the right edge.
    # That means: current_x <= window_width - EDGE_MARGIN - STEP
    # Example: width - 5 - 20 = width - 25 → check like x < (width - 24)
    def right(self):
        if self.current_position.x <= (
            self.window_width - self.EDGE_MARGIN - self.STEP
        ):
            self.pen.line_to(
                self.current_position.x + self.STEP, self.current_position.y
            )
