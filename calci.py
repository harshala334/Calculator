import tkinter as tk
from calcifunctions import *
# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display the result
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 14), justify='right')

entry.grid(row=0, column=0,columnspan=5, sticky='nsew')

# Buttons
buttons = [
    '7', '8', '9', '/','*',
    '4', '5', '6', '+','-',
    '1', '2', '3', '^','sqrt',
    '.', '0', 'sin', 'cos', 'tan',
    'C','Del','(',')', '='    
]

# Create and place buttons in the grid
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(root, text=button, font=('Arial', 18,'bold'),bg='light gray',fg='black', command=lambda b=button: on_button_click(entry_var,b)).grid(
        row=row_val, column=col_val, sticky='nsew')
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1
        

# Configure row and column weights
for i in range(0, 5):
    root.grid_columnconfigure(i, weight=1)
for i in range(1, 6):    
    root.grid_rowconfigure(i, weight=1)
for i in range(0,1):    
    root.grid_rowconfigure(i, weight=2)
    
# Run the Tkinter event loop
root.mainloop()
