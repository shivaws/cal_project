# calculator_wrapper.py

import os
from ctypes import CDLL, c_int

# Get the absolute path to the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load the shared library
library_path = os.path.join(current_dir, 'calculator.dylib')
calculator_lib = CDLL(library_path)

# Define the function signature for the calculate function
calculator_lib.calculate.argtypes = [c_int, c_int, c_int, c_int]
calculator_lib.calculate.restype = c_int

def calculate(num_one, num_two, num_three, choice):
    return calculator_lib.calculate(num_one, num_two, num_three, choice)
