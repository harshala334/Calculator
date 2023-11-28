import math
import tkinter as tk
# Function to handle addition
def add(entry_var):
    current_text = entry_var.get()
    entry_var.set(current_text + '+')

# Function to handle subtraction
def subtract(entry_var):
    current_text = entry_var.get()
    entry_var.set(current_text + '-')

# Function to handle multiplication
def multiply(entry_var):
    current_text = entry_var.get()
    entry_var.set(current_text + '*')

# Function to handle division
def divide(entry_var):
    current_text = entry_var.get()
    entry_var.set(current_text + '/')

# Function to handle square root
def square_root(entry_var):
    try:
        result = math.sqrt(float(entry_var.get()))
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

# Function to handle sine
def sine(entry_var):
    try:
        angle = float(entry_var.get())
        result = math.sin(math.radians(angle))
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

# Function to handle cosine
def cosine(entry_var):
    try:
        angle = float(entry_var.get())
        result = math.cos(math.radians(angle))
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

# Function to handle tangent
def tangent(entry_var):
    try:
        angle = float(entry_var.get())
        result = math.tan(math.radians(angle))
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

# Function to clear the entry
def clear_all(entry_var):
    entry_var.set("")

# Function to evaluate the expression
def evaluate(entry_var):
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except (SyntaxError, ZeroDivisionError, ValueError) as e:
        entry_var.set("Error")


def delete_last_character(entry_var):
    current_text = entry_var.get()
    entry_var.set(current_text[:-1])

def calculate_power(entry_var,button):
    try:
        expression = entry_var.get()
        if '^' in expression:
            base, exponent = expression.split('^')
            result = eval(f"{float(base)} ** {float(exponent + button)}")
            entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")
  

def on_button_click(entry_var,button):
    if button == '+':
        add(entry_var)
    elif button == '-':
        subtract(entry_var)
    elif button == '*':
        multiply(entry_var)
    elif button == '/':
        divide(entry_var)
    elif button == '=':
        evaluate(entry_var)
    elif button == 'sin':
        sine(entry_var)
    elif button == 'cos':
        cosine(entry_var)
    elif button == 'tan':
        tangent(entry_var)
    elif button == 'sqrt':
        square_root(entry_var)
    elif button == 'C':
        clear_all(entry_var)
    elif button == 'Del':
        delete_last_character(entry_var)
    elif '^' in entry_var.get():
        # If '^' is in the current expression, calculate the power
        calculate_power(entry_var,button)   
    else:
        entry_var.set(entry_var.get() + button)
