import os
import argparse

def get_files_list(folderpath):
    files_list = []
    for dirpath, subdirs, files in os.walk(folderpath):
        for file in files:
            filepath = os.path.join(dirpath, file)
            filesize = os.path.getsize(filepath)
            files_list.append((dirpath, file, filesize))
    return files_list

def find_dublicates(files_list):
    dublicated_files = []
    non_dublicated_files = []
    for dirpath, file, filesize in files_list:
        if (file, filesize) in non_dublicated_files:
            dublicated_files.append((dirpath, file))
        else:
            non_dublicated_files.append((file,filesize))
    return dublicated_files

def createParser():

    parser = argparse.ArgumentParser(prog = 'Search for duplicates',
                                     description = '''The script searches for dublicated files
in current working directory or any other directory (need to specify its absolute path). ''',
                                     epilog = '''(c) p-well 2017. The author of the program 
does not bear any responsibility.''')

    parser.add_argument('path_to_dir', nargs='?', default = current_dir_path, type=argparse.FileType())
    parsed_dirpath = parser.parse_args()
    return parsed_dirpath
	
if __name__ == '__main__':

    current_dir_path = os.getcwd() 
    parsed_dirpath = createParser()
    all_files_in_tree = get_files_list(parsed_dirpath.path_to_dir)
    dublicated_files = find_dublicates(all_files_in_tree)
    
    if len(dublicated_files) == 0:
        print('\nNo dublicated files have been found in this directory tree.')
    else:
        print('\nThe following files are dublicates: \n')
        for dubl_file in dublicated_files:
            print('Location: {}\tFile: {}'.format(dubl_file[0], dubl_file[1]))
