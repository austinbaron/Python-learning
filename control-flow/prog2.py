
'''
Program to check if the last digit of a number is divisible by 3 or not

'''

num=int(input("Enter the number"))
last_digit = num%10

if last_digit%3==0:
    print(f"last digit of a number {num} is divisible by 3")
else:
    print(f"last digit of a number {num} not divisible by 3")
    
