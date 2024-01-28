'''
Program to check if the entered number is 3 digit number or not
'''

num = input("enter the number =  ")
l = len(num)
if l!=3:
  print(f"the length of the entered number {num} is {l}")
else:
  print("its a 3 digit number")