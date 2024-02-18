import csv


rows = []
header = ['Name', 'M1 Score', 'M2 Score']
data = [['Alex', 62, 80], ['Brad', 45, 56], ['Joey', 85, 98]]

def readfile():
    file = open("test_data.csv", 'r')
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
        print(row[0])
    print(header)
    print(rows)

def writefile():
    filename = 'Students_Data.csv'
    with open(filename, 'w', newline="") as file:
        csvwriter = csv.writer(file) # 2. create a csvwriter object
        csvwriter.writerow(header) # 4. write the header
        csvwriter.writerows(data) # 5. write the rest of the data

readfile()
writefile()