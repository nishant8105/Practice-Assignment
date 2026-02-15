# Assignment 3 Report

This report documents the Python scripts created for Assignment 3, focusing on functions and mathematical modules.

## Task 1: Factorial Calculation (`Task1.py`)

### Description
This script is designed to calculate the factorial of a number using recursion. It defines a function `factorial(num)` that calls itself with `num - 1` until the base case of `num == 1` is reached.


### Explanation
1.  **Function Definition**: The `factorial` function checks if `num` is 1. If so, it returns 1 (base case). Otherwise, it returns `num` multiplied by `factorial(num - 1)`.
2.  **Input**: The user is prompted to enter a number.
3.  **Output**: The script calculates the factorial of the input number and prints the result.

## Task 2: Mathematical Operations (`Task2.py`)

### Description
This script demonstrates the use of the `math` module to perform various mathematical calculations such as square root, logarithm, and sine.


### Explanation
1.  **Import**: The `math` module is imported to access mathematical functions.
2.  **Input**: The user provides a number.
3.  **Calculations**:
    - `math.sqrt(number)`: Calculates the square root.
    - `math.log(number)`: Calculates the natural logarithm.
    - `math.sin(number)`: Calculates the sine of the number (in radians).
4.  **Output**: The results of these operations are printed to the console.
