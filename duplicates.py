import os


def copies_search(way_to_dir):
    dublicate_files_list = []
    full_ways=[]
    for root, dirs, files in os.walk(way_to_dir):
        for file in files:
            dublicate_files_list.append(file)
            full_ways.append(os.path.join(root,file))
    ssss = dict((x, dublicate_files_list.count(x)) for x in set(dublicate_files_list) if dublicate_files_list.count(x) > 1 )
    for value,key in ssss.items():
        print('Файл {0} повторяется {1} раза.'.format(value,key))
    print(full_ways)
    #for name in full_ways:
    #    print(os.path.getsize(name))
    print(dublicate_files_list)
    print(ssss)


if __name__ == '__main__':
    # way_to_dir = input('Please enter way to directory: ')
    copies_search('D:\\books')
