'''
Predefined functions to read a file
'''

def readfile():
    file = open("myfile1.txt","r+") 
    print("Output of the Read function is ")
    print(file.read())
    print()

def append():
    file1 = open("myfile1.txt","a")#append mode
    file1.write("Today \n")
    file1.close()

readfile()
append()