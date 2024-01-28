
### Decision-making Statements

Decision making statements are used in the Python programs to make them able to decide which of the alternative group of instructions to be executed, depending on value of a certain Boolean expression.

----

#### The if Statement

Python provides if..elif..else control statements as a part of decision marking.

```python
marks = 80 
result = ""
if marks < 30:
   result = "Failed"
elif marks > 75:
   result = "Passed with distinction"
else:
   result = "Passed"

print(result)

```

#### Loops or Iteration Statements

Most of the processes require a group of instructions to be repeatedly executed. In programming terminology, it is called a loop. Instead of the next step, if the flow is redirected towards any earlier step, it constitutes a loop.

> If the control goes back unconditionally, it forms an infinite loop which is not desired as the rest of the code would never get executed.

* For loop

```python
words = ["one", "two", "three"]
for x in words:
  print(x)

```

* While loop

```python

i = 1
while i < 6:
  print(i)
  i += 1

```