'''
Performing some basic reverse and file handling operation
'''

#open the file
text_file = open('myfile1.txt','r+')
l=[]

#get the list of line
line_list = text_file.readlines();

#for each line from the list, print the line
for line in line_list:
    #print(line[::-1])
    l.append("\n")
    l.append(line[::-1])

text_file.writelines(l)

text_file.close() #don't forget to close the file