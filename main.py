import tkinter as tk

# -----------------------------
# Functions
# -----------------------------
def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(value))


def clear_display():
    display.delete(0, tk.END)


def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])


def calculate():
    try:
        expression = display.get()
        # eveluate the string as python expression the most important function "evel"
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# -----------------------------
# Main Window
# -----------------------------
window = tk.Tk()
window.title("Basic Calculator")
window.geometry("340x500")
window.resizable(False, False)
window.configure(bg="#F2F2F2")

# -----------------------------
# Display
# -----------------------------
display = tk.Entry(
    window,
    font=("inter", 32),
    bd=5,
    relief="ridge",
    justify="right",
    bg= "#BECC71"

)

display.pack(fill="both", padx=10, pady=10, ipady=10)

# -----------------------------
# Button Frame
# -----------------------------
frame = tk.Frame(window, bg="#F2F2F2")
frame.pack()

buttons = [
    ['AC', 'CE', '%', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '=', '']
]

for r in range(len(buttons)):
    for c in range(len(buttons[r])):

        text = buttons[r][c]

        if text == "":
            continue

        # Button colors
        bg = "white"
        fg = "black"

        if text in ["=","0",".","1","2","3","4","5","6","7","8","9","*","%","/","-","+"]:
            bg = "#4C4949"
            fg = "white"   # Orange

        elif text == "AC":
            bg = "#FF6A00"   # Green
            fg = "white"

        elif text == "CE":
            bg = "#FF6A00"   # Red
            fg = "white"


        btn = tk.Button(
            frame,
            text=text,
            font=("Arial", 24, "bold"),
            width=3,
            height=1,
            bg=bg,
            fg=fg
        )
        if text == "+":
            btn.grid(row=r, column=c, rowspan=2,
                     padx=5, pady=5, sticky="nsew")
        else:
            btn.grid(row=r, column=c,
                     padx=5, pady=5, sticky="nsew")
    
        # Assign button actions
        if text == "=":
            btn.config(command=calculate)

        elif text == "AC":
            btn.config(command=clear_display)

        elif text == "CE":
            btn.config(command=backspace)

        else:
            btn.config(command=lambda t=text: button_click(t))

# -----------------------------
# Run Program
# -----------------------------
window.mainloop()