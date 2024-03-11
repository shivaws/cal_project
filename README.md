Step 1: "Execute the calculator.cpp" run using this command on your terminal **g++ -shared -o calculator.dylib -fPIC calculator.cpp**

Step 2: "After execution calculator.cpp we will get a file calculator.dylib (which is a shared library file generated after compiling your C++ code.) "

Step 3: "Use pip install ." to install the python lib

Step 4: "Use main.py" to execute the program in your terminal

**Explanation for calculator.cpp**

This C++ program serves as a basic calculator with a simple interface for performing mathematical operations. The program includes a function called calculate that takes four parameters:
* 		int num_one: The first number.
* 		int num_two: The second number.
* 		int num_three: The third number.
* 		int choice: An integer representing the user's choice of operation (1 for addition, 2 for subtraction, 3 for multiplication, and 4 for division).
The calculate function uses a switch statement to determine which operation to perform based on the choice parameter. Here's a breakdown of each case:
* Case 1 (Addition):  code result = num_one + num_two;
*    Adds num_one and num_two and stores the result in the variable result.
* Case 2 (Subtraction):  code result = num_one - num_two;
*    Subtracts num_two from num_one and stores the result in the variable result.
* Case 3 (Multiplication):  code result = num_one * num_two * num_three;
*    Multiplies num_one, num_two, and num_three and stores the result in the variable result.
* Case 4 (Division): code result = num_one / num_two;
*    Divides num_one by num_two and stores the result in the variable result. Before performing the division, it checks if num_two is zero to avoid division by zero, and if so, it prints an error message.
* Default Case:  code std::cout << "Please select the correct option from the above list." << std::endl;
* return -1;
*    If the user's choice is not 1, 2, 3, or 4, it prints an error message and returns -1 to indicate an error.
The calculate function returns the calculated result or -1 in case of an error.
The extern "C" is used to indicate that the function should have C-linkage to make it compatible with C programs or other languages this is often required when creating shared libraries to be used in other languages.

**Explanation for __init__.py** 

In Python, the `__init__.py` file is used to indicate that a directory should be treated as a Python package. This file can be empty or can contain Python code. Its presence allows the Python interpreter to recognize the directory as a package and enables the use of various package-related features.

Here are some key points about the `__init__.py` file:

1. **Package Initialization:**
   - When Python encounters a directory containing an `__init__.py` file, it treats the directory as a package.
   - The `__init__.py` file is executed during the package initialization, and it can contain initialization code or define variables that are needed for the package.

2. **Namespace Packages:**
   - The `__init__.py` file can also be used to define a namespace package. A namespace package is a package spread across multiple directories.
   - If a package consists of multiple directories, each directory can have its own `__init__.py` file, contributing to the overall namespace package.

3. **Explicit Initialization:**
   - The `__init__.py` file can be used to explicitly specify what gets imported when the package is imported using `import *`. This is done by defining the `__all__` variable in the `__init__.py` file.

4. **Python 3.3 and Later:**
   - In Python 3.3 and later versions, the `__init__.py` file is not strictly required for a directory to be considered a package. Implicit namespace packages can exist without an `__init__.py` file.
   - However, using `__init__.py` is still a common practice and provides a way to include package-specific initialization code.

5. **Package as a Module:**
   - The `__init__.py` file can also contain code that initializes the package as a module itself, providing a way to execute code when the package is imported.

Overall, the `__init__.py` file serves to define the behavior of a Python package and allows for package-specific customization and initialization. While not always strictly necessary, it is a convention followed in most Python projects.


**Explanation for calculator_wrapper.py**

The Python script calculator_wrapper.py serves as a bridge between the Python code and the C++ shared library (calculator.dylib). Here's an explanation of each part of the script:

Import Statements:

import os
from ctypes import CDLL, c_int
os: Provides a way to interact with the operating system, used here to get the current directory.
CDLL: A class from the ctypes module that loads dynamic link libraries (DLLs) or shared libraries.
Get the Absolute Path to the Current Directory:
current_dir = os.path.dirname(os.path.abspath(__file__))
os.path.abspath(__file__): Gets the absolute path of the current script.
os.path.dirname(...): Extracts the directory part of the path, giving the absolute path to the current directory.
Load the Shared Library (calculator.dylib):
library_path = os.path.join(current_dir, 'calculator.dylib')
calculator_lib = CDLL(library_path)
os.path.join(...): Combines the current directory path with the filename (calculator.dylib) to get the full path to the shared library.
CDLL(...): Loads the shared library into the script. calculator_lib is an instance of the CDLL class representing the loaded library.
Define the Function Signature:
calculator_lib.calculate.argtypes = [c_int, c_int, c_int, c_int]
calculator_lib.calculate.restype = c_int
argtypes: Specifies the argument types for the calculate function in the shared library (four integers in this case).
restype: Specifies the return type of the calculate function (integer).
Define the Python Function (calculate):
def calculate(num_one, num_two, num_three, choice):
    return calculator_lib.calculate(num_one, num_two, num_three, choice)
calculate A Python function that calls the calculate function from the loaded shared library, passing the provided arguments.
calculator_wrapper.py provides a convenient interface for Python code to interact with the C++ functionality implemented in the shared library. It loads the library, defines the function signature, and exposes a Python function (calculate) that internally calls the C++ function.

**Explanation for calculator.dylib**

`calculator.dylib` is a shared library file on macOS. The ".dylib" extension indicates that it is a dynamic library, which is a compiled binary file containing code and data that multiple programs can use simultaneously. In this context, it likely contains the compiled C++ code for the calculator functionality.
Shared libraries offer a way to share code among different programs, reducing redundancy and allowing for more efficient memory usage. The dynamic nature of these libraries means that they are loaded into memory only when needed, rather than being statically linked at compile time.
In your case, `calculator.dylib` appears to be the compiled version of the C++ code responsible for performing calculations, and it is loaded and used by the Python script through the `ctypes` module. This enables Python to access and utilize the C++ functionality defined in the shared library.

**Explanation for setup.py**

This Python script is a `setup.py` file, and it's used to package and distribute the C++ calculator program as a Python extension module. Let's break down the key components:

1. **Import Statements:**
   
   from setuptools import setup, find_packages, Extension
  
   - `setuptools`: A Python library for packaging and distribution.
   - `setup`: A function from `setuptools` used to configure the package.
   - `find_packages`: A function to automatically discover and include Python packages.
   - `Extension`: A class used to define C/C++ extension modules.

2. **Define the C++ Extension Module:**
   
   calculator_extension = Extension(
       'calculator',
       sources=['calculator.cpp'],
   )

   - `calculator_extension`: An instance of the `Extension` class defining the C++ extension module.
   - `'calculator'`: The name of the extension module that users will import in Python.
   - `sources=['calculator.cpp']`: The C++ source file (`calculator.cpp`) containing the implementation of the calculator functionality.

3. **Setup Configuration:**
   
   setup(
       name='calculator',
       version='1.0',
       packages=find_packages(),
       ext_modules=[calculator_extension],
   )
  
   - `name`: The name of the Python package.
   - `version`: The version number of the package.
   - `packages=find_packages()`: Automatically discover and include all Python packages in the distribution.
   - `ext_modules=[calculator_extension]`: Include the C++ extension module (`calculator_extension`) in the distribution.

This `setup.py` script is designed to be used with the `setuptools` package, which simplifies the process of packaging, distributing, and installing Python projects. When users run `python setup.py install`, it will compile the C++ code, create a shared library (extension module), and make it accessible as a Python package named 'calculator'. Users can then import and use this package in their Python scripts.

**Explanation for main.py**

This Python script is the main program that interacts with the C++ calculator functionality exposed through the extension module. Here's an explanation of the key components:

1. **Import Statement:**
   
   from calculator.calculator_wrapper import calculate
   
   - Imports the `calculate` function from the `calculator_wrapper` module, which is a Python interface to the C++ calculator functionality.

2. **User Input:**
   
   num_one = int(input("Enter your first number: "))
   num_two = int(input("Enter your second number: "))
   num_three = int(input("Enter your third number: "))
   
   - Prompts the user to enter three integer values for the calculator operation.

3. **Menu:**
   
   print("1) Addition")
   print("2) Subtraction")
   print("3) Multiplication")
   print("4) Division")
   choice = int(input("Enter your choice: "))
   
   - Displays a menu for the user to choose the type of calculation (addition, subtraction, multiplication, or division) and prompts the user to enter their choice.

4. **Calculate and Display Result:**
   
   result = calculate(num_one, num_two, num_three, choice)
   print("The result is:", result)
   
   - Calls the `calculate` function from the `calculator_wrapper` module, passing the user inputs and the chosen operation.
   - Prints the calculated result.

This script essentially acts as a user interface for the calculator functionality provided by the C++ code. It takes user inputs, interacts with the C++ code through the Python interface, and displays the calculated result. When executed, the user can perform various arithmetic operations using the underlying C++ functionality.





