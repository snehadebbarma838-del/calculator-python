import tkinter as tk

# ----- FUNCTIONS -----
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# ----- WINDOW -----
window = tk.Tk()
window.title("Calculator")
window.resizable(False, False)
window.configure(bg="#1e1e1e")

# ----- DISPLAY -----
entry = tk.Entry(
    window,
    width=16,
    font=("Arial", 28, "bold"),
    bg="#2d2d2d",
    fg="white",
    borderwidth=0,
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=15, pady=15, ipady=15)

# ----- BUTTON STYLE -----
def make_button(text, row, col, color="#3a3a3a", fg="white", colspan=1):
    btn = tk.Button(
        window,
        text=text,
        font=("Arial", 18, "bold"),
        bg=color,
        fg=fg,
        activebackground="#555",
        activeforeground="white",
        borderwidth=0,
        width=4,
        height=1,
        cursor="hand2"
    )
    btn.grid(row=row, column=col, columnspan=colspan,
             padx=6, pady=6, sticky="nsew")
    return btn

# ----- ROW 1 — AC, +/-, %, / -----
make_button("AC", 1, 0, "#a5a5a5", "black").config(command=clear)
make_button("+/-", 1, 1, "#a5a5a5", "black").config(
    command=lambda: button_click("-") if entry.get() == "" else None)
make_button("%", 1, 2, "#a5a5a5", "black").config(
    command=lambda: button_click("%"))
make_button("÷", 1, 3, "#ff9f0a").config(
    command=lambda: button_click("/"))

# ----- ROW 2 — 7, 8, 9, × -----
make_button("7", 2, 0).config(command=lambda: button_click("7"))
make_button("8", 2, 1).config(command=lambda: button_click("8"))
make_button("9", 2, 2).config(command=lambda: button_click("9"))
make_button("×", 2, 3, "#ff9f0a").config(
    command=lambda: button_click("*"))

# ----- ROW 3 — 4, 5, 6, - -----
make_button("4", 3, 0).config(command=lambda: button_click("4"))
make_button("5", 3, 1).config(command=lambda: button_click("5"))
make_button("6", 3, 2).config(command=lambda: button_click("6"))
make_button("-", 3, 3, "#ff9f0a").config(
    command=lambda: button_click("-"))

# ----- ROW 4 — 1, 2, 3, + -----
make_button("1", 4, 0).config(command=lambda: button_click("1"))
make_button("2", 4, 1).config(command=lambda: button_click("2"))
make_button("3", 4, 2).config(command=lambda: button_click("3"))
make_button("+", 4, 3, "#ff9f0a").config(
    command=lambda: button_click("+"))

# ----- ROW 5 — 0, ., ⌫, = -----
make_button("0", 5, 0, colspan=1).config(
    command=lambda: button_click("0"))
make_button(".", 5, 1).config(command=lambda: button_click("."))
make_button("⌫", 5, 2).config(command=backspace)
make_button("=", 5, 3, "#ff9f0a").config(command=calculate)

# ----- GRID SIZING -----
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

# ----- RUN -----
window.mainloop()