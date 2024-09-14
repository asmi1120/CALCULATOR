import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
        elif operation == '%':
            if num2 != 0:
                result = num1 % num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
        elif operation == '**':
            result = num1 ** num2
        elif operation == '//':
            result = num1 // num2
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")
root = tk.Tk()
root.title("Simple Calculator")
tk.Label(root, text="Enter the first number:").pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()
tk.Label(root, text="Enter the second number:").pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()
tk.Label(root, text="Choose operation:").pack()
operation_var = tk.StringVar(value='+')
tk.Radiobutton(root, text="+", variable=operation_var, value='+').pack()
tk.Radiobutton(root, text="-", variable=operation_var, value='-').pack()
tk.Radiobutton(root, text="*", variable=operation_var, value='*').pack()
tk.Radiobutton(root, text="/", variable=operation_var, value='/').pack()
tk.Radiobutton(root, text="%", variable=operation_var, value='%').pack()
tk.Radiobutton(root, text="**", variable=operation_var, value='**').pack()
tk.Radiobutton(root, text="//", variable=operation_var, value='//').pack()
tk.Button(root, text="Calculate", command=calculate).pack()
result_label = tk.Label(root, text="Result:")
result_label.pack()
root.mainloop()
