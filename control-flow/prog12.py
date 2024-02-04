'''
program that takes user input
'''
# Define the list
nums = []

# The loop will run while the length of the
# list nums is less than 4
while len(nums) < 4:
    # Ask for user input and store it in a variable as an integer.
    user_input = int(input("Enter an integer: "))
    # If the input is an even number, add it to the list
    if user_input % 2 == 0 and user_input > 0:
        nums.append(user_input)
    elif user_input == 0:
        continue ## iin case continue need to be use
else:
    print("the length of the list exceed, hence printing the list")

print(nums)