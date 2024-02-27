from os import listdir
import csv
import numpy as np

# Imports all the filenames in the folder
folder_name = str('..\\' + input("Folder name: "))
filenames = listdir(folder_name)

# Create empty lists for the final output files, both content and the 'header' which will be the full file names
all_data = []
column_name = []

# Ask for input which the code should sort for in the file names
namePart = str(input("Sorting string: "))

# Sorts through the file names and imports file contents
for i in range(len(filenames)): 
    if namePart in filenames[i]: 
        column_name.append(filenames[i])
        with open(str(filenames[i]), 'r') as filecontent: # Reads the contents of the files. Name of the output file will be the same as the 'sorting input'
            lines = filecontent.readlines()
            # temp is a temporary holder which takes the lines of the data file and splits everything into individual values, and formats it into floats with 6 decimal places
            temp = [list(map(lambda x: format(float(x), '05.6f'), line.strip('\n').split('\t'))) for line in lines]
            all_data.append(temp)

# all_data is a matrix with dimensions: nr_files * nr_datapoints * 2. The 2 comes from the x and y values in the file.
# Transposes the matrix to nr_datapoints * nr_files * 2.
transposed = list(map(list, zip(*all_data)))

# Writes the data to a new text file of tab separated values
with open(str(namePart), "w", newline='') as txt_file:
    for row in transposed:
        flatrow = [val for pair in row for val in pair] # flattens the rows so that xa1 ya1 xb1 yb1 xc1 yc1... etc all ends up as one long list
        line = "        ".join(map(lambda x: str(x).strip('[],'), flatrow)) # joins the values in each row into one long string
        txt_file.write(line + "\n")

# Takes the filenames and puts them into another txtfile
with open("columns" + str(namePart), "w") as txt_file:
    for i in range(len(column_name)):
        txt_file.write(column_name[i] + "       " + column_name[i] + '\t')
