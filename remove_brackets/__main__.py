from os import listdir, rename, chdir, getcwd
from os.path import isfile, join
from argparse import ArgumentParser
import logging
import re

# Equipped a logger for debugging
LOG_FORMAT = "[%(levelname)s] - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)

LOGGER = logging.getLogger()


def parse_arguments():
    desc = 'Removes brackets and content within brackets of file names.'
    parser = ArgumentParser(description=desc)
    parser.add_argument('folder', metavar='folder', nargs='?',
                        type=str, help='Target folder')
    # parser.add_argument('-r', '--recursion',
    #                    action='store_true', help='Enable recursion.')
    return parser.parse_args()


def remove_brackets(filename):
    """ Returns a string with the removed brackets and parentheses """
    return re.sub("([\(\[]).*?([\)\]])", "", filename)


def get_list_of_files(directory):
    return [filename for filename in listdir(directory) if isfile(join(directory, filename))]


def rename_files(old_list: list, new_list: list):
    for old_file, new_file in zip(old_list, new_list):
        try:
            if old_file == new_file:
                LOGGER.debug('Skipping:' + str(old_file))
            else:
                LOGGER.debug('Old: ' + str(old_file) +
                             ', New: ' + str(new_file))
                rename(old_file, new_file)
        except Exception as e:
            LOGGER.debug('ERROR:' + str(e))


def main():
    # List of startup arguments
    arguments = parse_arguments()

    # Change Working Directory to folder specified;
    # If no argument passed then use working directory
    if arguments.folder is None:
        path = getcwd()
    else:
        path = str(arguments.folder)
        if path == '.' or path == './':
            path = getcwd()

    chdir(path)

    # List of files with brackets
    files_with_brackets = get_list_of_files(path)
    #LOGGER.debug ('Before:' + files_with_brackets)

    # List of files without brackets
    files_without_brackets = [remove_brackets(
        singlefile) for singlefile in files_with_brackets]
    #LOGGER.debug ('After:' + files_without_brackets)

    LOGGER.debug('---- Starting to rename ----')
    rename_files(files_with_brackets, files_without_brackets)


if __name__ == '__main__':
    main()
