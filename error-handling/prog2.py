'''
An example showing that exception handling does not stop 
the execution of the code abruptly can be seen through the example below.
'''


try:
    f = open('test.txt', 'r')
except Exception as e:
    print(f'issue with the code {e}')

a = 1
b = 2
sum = a+b
print(f"sum of a and b is {sum}")