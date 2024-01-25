'''
Multiple variable assignment & Global local variables
'''
a = b = c = 10

print(a)
print(b)
print(c)

print("###--------------------###")

a,b,c= 45, 1000, "Cynefo"
print(f"{a} {b} {c}")

print("###-------------------###")

'''
Local Variable
'''
# local variable
def f():
##-------------------
    name="Cynefo-local" ## local variable 
    print(f"{name} is the local variable")
###-------------------

f()