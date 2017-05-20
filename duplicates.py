import os


def create_list_of_files_and_sizes(path_to_dir):
    convert_size_KB_to_MB = 2 ** 20
    if os.path.exists(path_to_dir):
        files_and_sizes = []
        for root_path, dirs, files, in os.walk(path_to_dir):
            for file in files:
                str_file_and_size = os.path.join(root_path, file)
                file_size = (os.path.getsize
                             (str_file_and_size)) / convert_size_KB_to_MB
                files_and_sizes.append(dict.fromkeys([file],
                                                     ("%.4f" % file_size)))
        return files_and_sizes


def copies_list(files_and_sizes):
    dublicates = []
    for file in files_and_sizes:
        if files_and_sizes.count(file) > 1:
            for key, value in file.items():
                dublicates.append((key, files_and_sizes.count(file)))
    return dublicates


def copies_print(dublicates):
    dublicates_list = set(dublicates)
    for dublicate in dublicates_list:
        print('File: {0}\n found {1} copies.\n'
              .format(dublicate[0], dublicate[1]))


if __name__ == '__main__':
    path_to_dir = input('Please enter directory: ')
    list_of_files_and_sizes = create_list_of_files_and_sizes(path_to_dir)
    if list_of_files_and_sizes:
        copies_print(copies_list(list_of_files_and_sizes))
    else:
        print('Some errors. Check that way to folder is correct ')
