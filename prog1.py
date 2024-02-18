'''
How to create a file
'''

def newfile():
    #creating a text file with the command function "x"
    f = open("myfile.txt", "x")



newfile()

'''
We've now created a new empty text file! 
But if you retry the code above – for example, 
if you try to create a new file with the same name as you used above (if you want to reuse the filename above) you will get an error
'''

'''
"w" – Write: this command will create a new text file whether or not there is a file in the memory with the new specified name. 
It does not return an error if it finds an existing file with the same name – instead it will overwrite the existing file.
'''

def existingfile():
    f = open("myfile.txt", "w")
    f.write("hello there\n")

existingfile()