import tkinter as tk
from canvas.canvas import TkPanel
from custom_turtle.turtle import Turtle


class App:
    def __init__(self, title="Default", height=400, width=400):
        # Create main Tkinter window
        self.window = tk.Tk()

        # Create a custom canvas (TkPanel) to draw on
        self.canvas = TkPanel(self.window, height, width)

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

    # Start the application
    def run(self):
        # Create a turtle linked to the canvas
        turtle = Turtle(self.canvas)
        self.turtle = turtle

        # Start Tkinter event loop (keeps window open and responsive)
        self.window.mainloop()
