import tkinter as tk
from tkinter import messagebox

def click(btn_text):
    current = entry.get()
    
    if btn_text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero")
        except Exception:
            messagebox.showerror("Error", "Invalid input")
    
    elif btn_text == "C":
        entry.delete(0, tk.END)
    
    else:
        entry.insert(tk.END, btn_text)

root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", "%", "C", "+"),
    ("=",)
]

for r, row in enumerate(buttons, start=1):
    for c, btn_text in enumerate(row):
        btn = tk.Button(
            root, text=btn_text, width=5, height=2,
            font=("Arial", 20),
            command=lambda text=btn_text: click(text)
        )
        btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)


root.mainloop()