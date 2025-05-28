from calc import *
import tkinter as tk
from tkinter import messagebox

def on_calculate():
    calcIn = entry.get()
    try:
        result = calc(calcIn)
        #entry.delete(0, tk.END)
        #entry.insert(tk.END, f"{calcIn} = {str(result)}")
        messagebox.showinfo("RESULT:", result)
    except Exception as e:
        messagebox.showerror("Error", str(e))
# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("500x200")

# Create and place the input field
test = tk.Label(root, text="Enter your calculation:")
test.grid(row=0, column=0, pady=5)
entry = tk.Entry(root, width=50)
entry.grid(row=0, column=1, columnspan=3, pady=5)



def insert_text(text):
    entry.insert(tk.END, text)
def delete_text():
    entry.delete(0, tk.END)

# Row 4
calc0_button = tk.Button(root, text="   0   ", command=lambda: insert_text("0"))
calc0_button.grid(row=4, column=0, columnspan=3, padx=1, pady=1)
calcPO_button = tk.Button(root, text="   (    ", command=lambda: insert_text("( "))
calcPO_button.grid(row=4, column=1, columnspan=2, padx=1, pady=1)
calcPC_button = tk.Button(root, text="    )   ", command=lambda: insert_text(" )"))
calcPC_button.grid(row=4, column=2, columnspan=1, padx=1, pady=1)
calcS_button = tk.Button(root, text="   -   ", command=lambda: insert_text(" - "))
calcS_button.grid(row=4, column=3, columnspan=2, padx=1, pady=1)
# Row 3
calc1_button = tk.Button(root, text="   1   ", command=lambda: insert_text("1"))
calc1_button.grid(row=3, column=0, columnspan=3, padx=1, pady=1)
calc2_button = tk.Button(root, text="   2   ", command=lambda: insert_text("2"))
calc2_button.grid(row=3, column=1, columnspan=2, padx=1, pady=1)
calc3_button = tk.Button(root, text="   3   ", command=lambda: insert_text("3"))
calc3_button.grid(row=3, column=2, columnspan=1, padx=1, pady=1)
calcP_button = tk.Button(root, text="   +  ", command=lambda: insert_text(" + "))
calcP_button.grid(row=3, column=3, columnspan=2, padx=1, pady=1)
# Row 2
calc4_button = tk.Button(root, text="   4   ", command=lambda: insert_text("4"))
calc4_button.grid(row=2, column=0, columnspan=3, padx=1, pady=1)
calc5_button = tk.Button(root, text="   5   ", command=lambda: insert_text("5"))
calc5_button.grid(row=2, column=1, columnspan=2, padx=1, pady=1)
calc6_button = tk.Button(root, text="   6   ", command=lambda: insert_text("6"))
calc6_button.grid(row=2, column=2, columnspan=1, padx=1, pady=1)
calcD_button = tk.Button(root, text="   /   ", command=lambda: insert_text(" / "))
calcD_button.grid(row=2, column=3, columnspan=2, padx=1, pady=1)
# Row 1
calc7_button = tk.Button(root, text="   7   ", command=lambda: insert_text("7"))
calc7_button.grid(row=1, column=0, columnspan=3, padx=1, pady=1)
calc8_button = tk.Button(root, text="   8   ", command=lambda: insert_text("8"))
calc8_button.grid(row=1, column=1, columnspan=2, padx=1, pady=1)
calc9_button = tk.Button(root, text="   9   ", command=lambda: insert_text("9"))
calc9_button.grid(row=1, column=2, columnspan=1, padx=1, pady=1)
calcM_button = tk.Button(root, text="   *   ", command=lambda: insert_text(" * "))
calcM_button.grid(row=1, column=3, columnspan=2, padx=1, pady=1)
# Calculate button!
calc_button = tk.Button(root, text="Calculate", command=on_calculate)
calc_button.grid(row=5, column=1, columnspan=1, pady=10)
calc_button = tk.Button(root, text="C/A", command=lambda: delete_text())
calc_button.grid(row=5, column=2, columnspan=1, pady=10)

# Run the application
root.mainloop()