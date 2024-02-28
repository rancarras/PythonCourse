from os import listdir

# Reads and formats the data
def read_file_content(filename):
    with open(filename, 'r') as filecontent:
        lines = filecontent.readlines()
        return [list(map(lambda x: '{:012.6f}'.format(float(x)), line.strip('\n').split('\t'))) for line in lines]

def main():
    # Imports all the filenames in the folder
    folder_name = str('..\\' + input("Folder name: "))
    filenames = listdir(folder_name)

    # Create empty lists for the final output files, both content and the 'header' which will be the full file names
    all_data = []
    column_name = []

    # Ask for input which the code should sort for in the file names
    name_part = str(input("Sorting string: "))

    # Sorts through the file names and imports file contents
    for filename in filenames:
        if name_part in filename:
            column_name.append(filename)
            all_data.append(read_file_content(filename))

    # Transposes the matrix to nr_datapoints * nr_files * 2.
    transposed = list(map(list, zip(*all_data)))

    # Writes the data to a new text file of tab-separated values
    with open(str(name_part), "w", newline='') as txt_file:
        for row in transposed:
            flat_row = [val for pair in row for val in pair]
            line = "        ".join(map(lambda x: str(x).strip('[],'), flat_row))
            txt_file.write(line + "\n")

    # Takes the filenames and puts them into another txt file
    formatted_names = [f"{name:15}" for name in column_name]
    with open("columns" + str(name_part), "w") as txt_file:
        for i in range(len(formatted_names)):
            txt_file.write(formatted_names[i] + "       " + formatted_names[i] + '\t')

if __name__ == "__main__":
    main()