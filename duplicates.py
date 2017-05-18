import os


def create_list_of_files_and_sizes(path_to_dir):
    convert_values = 2 ** 20
    if os.path.exists(path_to_dir):
        files_and_sizes = []
        for root_path, dirs, files, in os.walk(path_to_dir):
            for file in files:
                str_file_and_size = os.path.join(root_path, file)
                file_size = (os.path.getsize(str_file_and_size))/convert_values
                files_and_sizes.append("'{}' size: {} MB\n".
                                       format(file, ("%.4f" % file_size)))
        return files_and_sizes


def copies_search(files_and_sizes):
    available_copies = 1
    dict_of_doubles = dict((file, files_and_sizes.count(file))
                           for file in set(files_and_sizes)
                           if files_and_sizes.count(file) > available_copies)
    return dict_of_doubles


def copies_print(dict_of_doubles):
    for value, key in dict_of_doubles.items():
        print('File: {0} found {1} copies.\n'.format(value, key))


if __name__ == '__main__':
    path_to_dir = input('Please enter directory: ')
    list_of_files_and_sizes = create_list_of_files_and_sizes(path_to_dir)
    if list_of_files_and_sizes:
        copies_print(copies_search(list_of_files_and_sizes))
    else:
        print('Some errors. Check that way to folder is correct ')
