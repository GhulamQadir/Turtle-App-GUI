import tkinter as tk


class TkPanel(tk.Canvas):
    def __init__(self, master=None, h=400, w=400):
        # Initialize a Tkinter Canvas with custom height and width
        super().__init__(master, height=h, width=w)
        # Create a button widget inside the given master (window/canvas)
        self.my_button = tk.Button(
            master,
            bg="brown",
            font=("Arial", 10, "bold"),
            fg="white",
            text="Clear",
            command=self.clear_window,
        )
        # Place the button at the top-right corner of the window
        self.my_button.pack(side="top", anchor="ne")
        # Store all drawn lines for reference
        self.lines = []

    # Add a new line object to the panel and draw it
    def add_line(self, line):
        self.lines.append(line)  # keep record of the line
        self.draw(line)  # actually draw it on the canvas

    # Draw a single line on the canvas using tkinter's create_line()
    def draw(self, line):
        self.create_line(
            line.start_point.x,
            line.start_point.y,  # starting coordinates
            line.end_point.x,
            line.end_point.y,  # ending coordinates
        )

    def clear_window(self):
        self.delete("all")
        self.lines = []
