import os
import numpy as np

def normalize_data(data):
    data_array = np.array(data)
    x, y = data_array[:, 0], data_array[:, 1]
    y = y.astype(float)
    norm_y = (y - np.min(y)) / (np.max(y) - np.min(y))
    normalized_data = np.column_stack((x, norm_y))
    return normalized_data

def import_files(folder_name, name_part):
    filenames = [file for file in os.listdir(folder_name) if name_part in file]
    all_data = []
    column_names = []

    for filename in filenames:
        column_names.append(filename)
        with open(filename, 'r') as file_content:
            lines = file_content.readlines()
            temp = [list(map(lambda x: '{:012.6f}'.format(float(x)), line.strip('\n').split('\t'))) for line in lines]
            all_data.append(temp)

    return column_names, all_data

def write_data_to_file(name_part, transposed_data):
    with open(name_part, "w", newline='') as txt_file:
        for row in transposed_data:
            formatted_row = ['{:012.6f}'.format(float(val)) for pair in row for val in pair]
            line = "        ".join(formatted_row)
            txt_file.write(line + "\n")

def write_column_names_to_file(formatted_names, output_filename):
    with open(output_filename, "w") as txt_file:
        for name in formatted_names:
            txt_file.write(name + "       " + name + '\t')

def main():
    folder_name = str('..\\' + input("Folder name: "))
    name_part = str(input("Sorting string: "))

    column_names, all_data = import_files(folder_name, name_part)
    norm_matrix = [normalize_data(data) for data in all_data]

    # Transpose the matrix
    transposed_matrix = list(map(list, zip(*norm_matrix)))

    # Write data to a new text file
    write_data_to_file(name_part, transposed_matrix)

    # Write column names to another text file
    formatted_names = [f"{name:15}" for name in column_names]
    write_column_names_to_file(formatted_names, "columns" + str(name_part))

if __name__ == "__main__":
    main()
