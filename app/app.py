import tkinter as tk
from canvas.canvas import TkPanel
from custom_turtle.turtle import Turtle


class App:
    def __init__(self, title="Default", height=400, width=400):
        # Create main Tkinter window
        self.window = tk.Tk()

        # Validate and adjust the window size if it's too small or too large
        # Ensures minimum and maximum bounds for both height and width
        self.height, self.width = self.validate_window_size(height, width)

        # Create a custom canvas (TkPanel) to draw on
        self.canvas = TkPanel(self.window, self.height, self.width)

        # Display and arrange the canvas inside the main window
        self.canvas.pack()

        # Set the window title
        self.window.title(title)

        # Turtle will be created later in run()
        self.turtle = None

        # Bind keyboard events to key_press callback
        # Any key press will call self.key_press(event)
        self.window.bind("<Key>", self.key_press)

    # Handle key press events (arrow keys)
    def key_press(self, event):
        key = event.keysym  # event.keysym gives the key name (e.g., 'Up', 'Down')
        if key == "Up":
            self.turtle.forward()
        elif key == "Down":
            self.turtle.backward()
        elif key == "Left":
            self.turtle.left()
        elif key == "Right":
            self.turtle.right()

    def validate_window_size(self, height, width):
        """
        Validate and adjust the window size:
        - Minimum allowed height = 400
        - Maximum allowed height = 495
        - Minimum allowed width  = 400
        - Maximum allowed width  = 995
        If values are outside these ranges, they are clamped (adjusted to fit).
        """
        if height < 400:
            height = 400
        elif height > 495:
            height = 495
        if width < 400:
            width = 400
        elif width > 995:
            width = 995
        return height, width

    # Start the application
    def run(self):
        # Create a turtle linked to the canvas
        turtle = Turtle(self.canvas)
        self.turtle = turtle

        # Start Tkinter event loop (keeps window open and responsive)
        self.window.mainloop()
