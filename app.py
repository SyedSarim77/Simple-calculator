import streamlit as st

# Function definitions for the calculator operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Streamlit app layout
st.title("Simple Calculator")

# Input fields for user numbers
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Dropdown menu for selecting operation
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

# Calculate and display the result
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)

    st.write(f"Result: {result}")
# Simple-calculator
This is a simple Calculator using Python.
