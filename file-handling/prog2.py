'''
Program to use pre-defined functions
'''

'''
The writelines() method:
This function inserts multiple strings at the same time. 
A list of string elements is created, and each string is then added to the text file.

'''


def func():
    f = open("myfile1.txt", "w")
    L = ["Hello World\n", "You are welcome to Cynefo\n"]
    f.writelines(L)
    print("Is this file writable when opened in 'write' mode? ", f.writable())

func()