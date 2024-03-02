### Python Basics

#### [Variables](./variables)

Python Variable is containers that store values. Python is not “statically typed”. We do not need to declare variables before using them or declare their type. A variable is created the moment we first assign a value to it. A Python variable is a name given to a memory location.

* Rules for Python variables

    1. A Python variable name must start with a letter or the underscore character.
    2. A Python variable name cannot start with a number.
    3. A Python variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
    4. Variable in Python names are case-sensitive (name, Name, and NAME are three different variables).
    5. The reserved words(keywords) in Python cannot be used to name the variable in Python.

#### [Data Types](./data-types/data-file.md)

Data types are the classification or categorization of data items. It represents the kind of value that tells what operations can be performed on a particular data. Since everything is an object in Python programming, data types are classes and variables are instances (objects) of these classes. The following are the standard or built-in data types in Python:

1. Numeric
2. Sequence Type
3. Boolean
4. Set
5. Dictionary
6. Binary Types( memoryview, bytearray, bytes)

![data-types](./images/Python-data-structure.jpg)

#### [Control Flow](./control-flow/README.md)

Python program control flow is regulated by various types of conditional statements, loops, and function calls. By default, the instructions in a computer program are executed in a sequential manner, from top to bottom, or from start to end. 

#### [Functions](./functions/README.md)

You use functions in programming to bundle a set of instructions that you want to use repeatedly or that, because of their complexity, are better self-contained in a sub-program and called when needed. That means that a function is a piece of code written to carry out a specified task. To carry out that specific task, the function might or might not need multiple inputs. When the task is carried out, the function can or can not return one or more values.

There are three types of functions in Python:

* Built-in functions, such as help() to ask for help, min() to get the minimum value, print() to print an object to the terminal,… You can find an overview with more of these functions here.
* User-Defined Functions (UDFs), which are functions that users create to help them out; And
* Anonymous functions, which are also called lambda functions because they are not declared with the standard def keyword.

#### [File Handling](./file-handling/README.md)

File handling in Python is an important part of any web application. Python offers several functions for opening, reading, creating, writing, closing, or deleting files in python

Basics of file handling in Python:

* Open a file 
* Read/write/create/delete
* Close a file

#### [Exception Handling](./error-handling/README.md)

Exception Handling is a crcial concept in python which allows us to gracefully handle and manage the errors and exceptional situations which may occur during the program execution.

#### [Modules](./module/README.md)

The concept of module in Python further enhances the modularity. You can define more than one related functions together and load required functions. A module is a file containing definition of functions, classes, variables, constants or any other Python object. Contents of this file can be made available to any other program. Python has the import keyword for this purpose.