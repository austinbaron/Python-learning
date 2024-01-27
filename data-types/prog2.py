'''
List Data type
'''

#list of having both integers and strings
c= ["hey","you",1,2,3,"go"]
print(c)

#index are 0 based. this will print a single character
print(c[1]) #this will print "you" in list c

## Inserting a string at 0 index 
c.insert(0, "cynefo")

## Inserting a string at last index 
c.insert(len(c), "cynefohub")

print(c)

## Deletion of an element from the list
c.remove("go")
print(c)

c.pop()
print(c)

####-----------

'''
Tuple Data type
'''
# a=(1,2,3,4)
# print(a) #prints the whole tuple

# #tuple having multiple type of data.
# b=("hello", 1,2,3,"go")
# print(b) #prints the whole tuple

# #index of tuples are also 0 based.

# print(b[4]) #this prints a single element in a tuple, in this case "go"
