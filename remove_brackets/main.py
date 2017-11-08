from os import listdir, rename, chdir
from os.path import isfile, join

import re

DIRECTORY_TO_CHANGE = r'path/to/folder'

chdir(DIRECTORY_TO_CHANGE)

def remove_brackets(filename):
    return re.sub("([\(\[]).*?([\)\]])", "", filename)

def get_list_of_files(directory):
    return [filename for filename in listdir(directory) if isfile(join(directory, filename))]

def rename_files(old_list: list, new_list: list):
    for old_file, new_file in zip(old_list, new_list):
        try:
            if old_file == new_file:
                print ('Skipping:', old_file)
            else:
                print ('Old:', old_file, ', New', new_file)
                rename(old_file, new_file)
        except Exception as e:
            print ('ERROR:', e)

def main():
    files_with_brackets = get_list_of_files(DIRECTORY_TO_CHANGE)
    #print ('Before:', files_with_brackets)

    files_without_brackets = [remove_brackets(singlefile) for singlefile in files_with_brackets]
    #print ('After:', files_without_brackets)

    print ('----Starting to rename ----')
    rename_files(files_with_brackets, files_without_brackets)





if __name__ == '__main__':
    main()
