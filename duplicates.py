import os


def copies_search(way_to_dir):
    path_f=[]
    dublicate_files_list=[]
    for root, dirs, files in os.walk(way_to_dir):
        for file in files:
            #path=os.path.join(file)
            #path = os.path.join(root)
            path_f.append(file)
            #path_f.insert(n + 1, os.path.join(root))
    print('Повторяющиеся элементы:')
    for files in path_f:
        if path_f.count(files)>1:
            dublicate_files_list.append(files)
    set(dublicate_files_list)
    array_length=len(dublicate_files_list)
    for k in range(array_length):
        print(dublicate_files_list[k])



if __name__ == '__main__':
    #way_to_dir = input('Please enter way to directory: ')
    copies_search('D:\\books')

