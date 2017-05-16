import os


def create_list_of_files_and_sizes(way_to_dir):
    testing_list = []
    for root, dirs, files, in os.walk(way_to_dir):
        for file in files:
            file_size = os.path.getsize(os.path.join(root, file))
            testing_list.append("{} имеющий размер: {} мегабайт".format(file, ("%.4f" % (file_size / 2 ** 20))))
    return testing_list


def copies_search():
    dict_of_doubles = dict((x, testing_list.count(x)) for x in set(testing_list) if testing_list.count(x) > 1)
    for value, key in dict_of_doubles.items():
        print('Файл {0} повторяется {1} раза.'.format(value, key))
    print(dict_of_doubles)

def copies_print():
    pass


if __name__ == '__main__':
    # way_to_dir = input('Please enter way to directory: ')
    create_list_of_files_and_sizes('D:\\books')
