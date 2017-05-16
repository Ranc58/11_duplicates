import os
import sys


def input_search_output():
    way_to_dir = input('Please enter directory or type "exit" to exit: ')
    if way_to_dir != 'exit':
        list_of_files_and_sizes = create_list_of_files_and_sizes(way_to_dir)
        copies_print(copies_search(list_of_files_and_sizes)) \
            if list_of_files_and_sizes is not None else \
            print('Some errors. Check that ways to folder is correct '), \
            input_search_output()
    else:
        print('GoodBye!')
        sys.exit()


def create_list_of_files_and_sizes(way_to_dir):
    if os.path.exists(way_to_dir):
        list_of_files_and_sizes = []
        for root, dirs, files, in os.walk(way_to_dir):
            for file in files:
                file_size = \
                    (os.path.getsize(os.path.join(root, file))) / 2 ** 20
                list_of_files_and_sizes \
                    .append("'{}' size: {} MB\n"
                            .format(file, ("%.4f" % file_size)))
        return list_of_files_and_sizes


def copies_search(list_of_files_and_sizes):
    dict_of_doubles = dict((file, list_of_files_and_sizes.count(file))
                           for file in set(list_of_files_and_sizes)
                           if list_of_files_and_sizes.count(file) > 1)
    return dict_of_doubles


def copies_print(dict_of_doubles):
    for value, key in dict_of_doubles.items():
        print('File: {0} found {1} copies.\n'.format(value, key))


if __name__ == '__main__':
    input_search_output()
