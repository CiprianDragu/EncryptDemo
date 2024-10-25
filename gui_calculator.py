import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

      # Create app

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        # Create entry widgets
        self.num1_entry = tk.Entry(master)
        self.num2_entry = tk.Entry(master)

        # Create operation buttons
        self.add_button = tk.Button(master, text="Add", command=lambda: self.calculate(add))
        self.subtract_button = tk.Button(master, text="Subtract", command=lambda: self.calculate(subtract))
        self.multiply_button = tk.Button(master, text="Multiply", command=lambda: self.calculate(multiply))
        self.divide_button = tk.Button(master, text="Divide", command=lambda: self.calculate(divide))

        # Create result label
        self.result_label = tk.Label(master, text="Result: ")

        # Grid layout
        self.num1_entry.grid(row=0, column=0, padx=5, pady=5)
        self.num2_entry.grid(row=0, column=1, padx=5, pady=5)
        self.add_button.grid(row=1, column=0, padx=5, pady=5)
        self.subtract_button.grid(row=1, column=1, padx=5, pady=5)
        self.multiply_button.grid(row=2, column=0, padx=5, pady=5)
        self.divide_button.grid(row=2, column=1, padx=5, pady=5)
        self.result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def calculate(self, operation):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            result = operation(num1, num2)
            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Create the main window and run the app
root = tk.Tk()
app = CalculatorApp(root)
root.mainloop()