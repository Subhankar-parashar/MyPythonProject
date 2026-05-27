import tkinter as tk
from tkinter import simpledialog, messagebox

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

a = simpledialog.askstring("Input", "Enter first number:")
operation = simpledialog.askstring(
    "Operation",
    "Enter operation (sum, sub, mul, div, average, factorial, percentage):"
)

if operation == "factorial":
    result = factorial(int(a))
else:
    b = simpledialog.askstring("Input", "Enter second number:")

    if operation == "sum":
        result = float(a) + float(b)

    elif operation == "sub":
        result = float(a) - float(b)

    elif operation == "mul":
        result = float(a) * float(b)

    elif operation == "div":
        result = float(a) / float(b)

    elif operation == "average":
        result = (float(a) + float(b)) / 2

    elif operation == "percentage":
        result = (float(a) / float(b)) * 100

    else:
        result = "Invalid operation"

messagebox.showinfo("Result", f"Answer = {result}")