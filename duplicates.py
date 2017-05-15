import os
from collections import Counter


def copies_search(way_to_dir):
    path_f = []
    dublicate_files_list = []
    for root, dirs, files in os.walk(way_to_dir):
        for file in files:
            dublicate_files_list.append(file)
    for name_h in dublicate_files_list:
        if name_h in dublicate_files_list:
            path_f.append(name_h)
    ssss = dict((x, path_f.count(x)) for x in set(path_f) if path_f.count(x) > 1)
    for key in ssss:
        print('Файл %s повторяется %s раза.' % (key, ssss[key]))

    """
    for root, dirs, files in os.listdir(path=way_to_dir):
        for file in files:
            path_f.append(file)
    print('Повторяющиеся элементы:')
    
    for files in path_f:
        if path_f.count(files)>1:
            dublicate_files_list.append(files)
    set(dublicate_files_list)
    array_length=len(dublicate_files_list)
    for k in range(array_length):
        print(type(dublicate_files_list[k]))
    print(dublicate_files_list)
    """


if __name__ == '__main__':
    # way_to_dir = input('Please enter way to directory: ')
    copies_search('D:\\books')
