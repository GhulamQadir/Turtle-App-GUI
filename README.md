# 🐢 Turtle Drawing App (Tkinter GUI)

This is a simple **Turtle-like drawing application** built with **Python** and **Tkinter**.  
It mimics the behavior of the classic Python `turtle` module but is implemented from scratch using **Object-Oriented Programming (OOP)** concepts.  

You can move the turtle (a virtual pen) using **arrow keys** and draw lines on a canvas.  

---

## 📂 Project Structure
Turtle-app-GUI/
│
├── main.py # Entry point of the application
│
├── app/
│ └── app.py # Defines App class (main GUI logic)
│
├── canvas/
│ └── canvas.py # TkPanel class (custom tkinter.Canvas for drawing lines)
│
├── custom_turtle/
│ └── turtle.py # Turtle class (controls movement & uses Pen)
│
├── geometry/
│ ├── line/
│ │ └── line.py # Line class (represents a line with start & end points)
│ ├── point/
│ │ └── point.py # Point class (represents x, y coordinates)
│ └── pen/
│ └── pen.py # Pen class (moves and draws lines on canvas)


---

## 🚀 How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/GhulamQadir/Turtle-App-GUI.git
cd Turtle-app-GUI

2. Install Python

Make sure you have Python 3.8+ installed.
Check with:

python --version

3. Run the Application

Execute the program with:

python main.py

🎮 How It Works

The app opens a Tkinter window with a white canvas.

A turtle (pen) starts at a default position.

You control the turtle using keyboard arrow keys:

⬆️ Up → Move forward (draws upward)

⬇️ Down → Move backward (draws downward)

⬅️ Left → Move left

➡️ Right → Move right

Each movement draws a line on the canvas.

A Clear button (top-right) can reset the canvas.

🛠 Features

✅ OOP-based design (Point, Line, Pen, Turtle, TkPanel, App classes)

✅ Uses @property for clean attribute access

✅ Arrow-key movement & drawing

✅ Clear button to erase canvas

🔮 Future Improvements

Add pen colors (change line color while drawing)

Add line thickness control

Save canvas as an image (PNG/JPG)

    Undo/Redo functionality

👨‍💻 Author

Ghulam Qadir 


