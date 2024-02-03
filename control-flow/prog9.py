'''
Break Statement

we have a list of numbers and we want to check if a number is present or not
'''

nums = [1, 2, 3, 4, 5, 6]

n = 2

found = False ## setting up flag
for num in nums:
    if n == num:
        found = True
        break

print(f'List contains {n}: {found}')

# Output
# List contains 2: True