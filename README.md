# compilers2025-forth_project-Nor88
Forth-to-C Compiler

Overview

This project is a Forth-to-C compiler that translates simple Forth code into equivalent C code. The generated C code performs operations on a stack, supporting a small set of Forth operations like basic arithmetic, conditionals, and stack manipulation.

The goal of the project is to demonstrate how a stack-based language like Forth can be compiled into a more widely-used language like C. This project can be extended to support additional Forth features, optimizations, and error handling.

Features

Translates basic Forth operations (push, pop, top, arithmetic operations, conditionals) into C code.
Supports defining custom Forth words (: ;).
Generates efficient C code to emulate stack operations and perform calculations.
Can be compiled and executed with a simple C compiler (e.g., GCC).
Table of Contents

Project Setup
Supported Forth Syntax
Generated C Code Structure
How to Use the Compiler
Contributing
License
Project Setup

Prerequisites
Before running the compiler, make sure you have the following installed:

Python 3: Required for running the Forth-to-C compiler.
GCC: Required for compiling the generated C code.
Installation
Clone this repository:
git clone https://github.com/yourusername/forth-to-c-compiler.git
cd forth-to-c-compiler
Install any Python dependencies (if any) by using pip:
pip install -r requirements.txt  # if you have a requirements.txt file
Make sure you have GCC installed:
sudo apt-get install gcc   # On Debian/Ubuntu-based systems
Supported Forth Syntax

The compiler supports the following Forth syntax:

Stack Operations
push <value>
Pushes a value onto the stack.
Pops the top value from the stack.
Retrieves the top value from the stack without removing it.
Adds the top two values of the stack and pushes the result.
Subtracts the top two values of the stack and pushes the result.
Multiplies the top two values of the stack and pushes the result.
Divides the top two values of the stack and pushes the result.

Conditionals
if
Executes the next block if the top of the stack is non-zero.

else
Executes the else block if the if condition was not satisfied.

endif
Marks the end of the if block.

Word Definition
: <word_name> ... ;
Defines a new custom Forth word.
