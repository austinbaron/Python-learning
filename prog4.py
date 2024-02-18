'''
Performing some basic operation
'''

#open the file
text_file = open('myfile1.txt','r')

#get the list of line
line_list = text_file.readlines();

#for each line from the list, print the line
for line in line_list:
    print(line)
    if "Hello World" in line:
        break

text_file.close() #don't forget to close the file