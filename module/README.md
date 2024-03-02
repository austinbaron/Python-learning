
### Modules
As our program grows bigger, it may contain many lines of code. Instead of putting everything in a single file, we can use modules to separate codes in separate files as per their functionality. This makes our code organized and easier to maintain.

Module is a file that contains code to perform a specific task. A module may contain variables, functions, classes etc

#### Example 1
[Example 1](./example1/) has a mymodule.py which prints the greeting msg

```python
def greeting(name):
  print("Hello, " + name)

```

#### Example 2
[Example 2](./example2/) has a set data type and explains how to reterive a specific value

```python
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

```

```python
from mymodule import person1

a = person1["age"]
print(a

```

#### Example 3
[Example 3](./example3/) explains built-in python module 