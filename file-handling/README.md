
### File handling
When you write any Python program, you save it in a file, and each file has its unique name and file extension. Files permanently store the data in non-volatile memory. Python allows users to handle the file, i.e., you can open, read, write, delete, or close files.

Basics of file handling in Python:

* Open a file 
* Read/write/create/delete
* Close a file

Apart from the most commonly used file handling functions: open(), read(), write(), and close(), there are a lot more functions that are used for file handling in Python.
Here is a list of some commonly used file-handling functions in Python.

| Function | Description |
|--|--|
| open() | Used to open a file. |
| readable() | Used to check whether the file can be read or not. |
| readline() | Used to read a single line from the file. |
| readlines() | Used to read all the content in the form of lines. |
| read() | Used to read whole content at a time. |
| writable() | Used to check whether the file is writable or not. |
| write() | Used to write a string to the file. |
| writelines() | Used to write multiple strings at a time. |
| close() | Used to close the file from the program. |

There are certain Access Mode as well for accessing the files

| Mode | Description |
| -- | -- |
| r | Read Mode (default value)|
| w| Write Mode (file is opened in write-only mode)|
| a| Append Mode (Opens a file for appending at the end of the file without truncating)|
| x| Create Mode (Creates a new file but will return an error if the file already exists.|
| t| Open the file in text mode.|
| b| Opens the file in binary mode.Binary mode returns bytes. It is mainly used while dealing with the non-text file such as images.|
| +| Opens the file for updating (reading and writing)|

Few Read Operations

```python
#read a file

nl = open('nl.txt','r') # it will open the file in read mode
nl.readline() # it will read the first line of the file
nl.read(10) # it will read the first 10 charcter of the file
nl.read() # it will return the whole text

```
Create a New File

```python

#create a file

nl = open ('nl.txt', 'x') # it will create a new empty file but will throw an error if the same file name exists
nl = open ('nl.txt', 'w') # it will create a file but if the same file name exist it will overwrite

```

Write in an existing file

```python

# write into an existing file

with open('nl.txt','w') as nl:
    nl.write('This is the first line\n')
    nl.write('This is the second line\n')
    nl.write('this is the third line')

```