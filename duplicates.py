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

def create_parser():
<<<<<<< HEAD
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_dir')
    dirpath = parser.parse_args()
    return dirpath
    
def print_results(dublicated_files):
    if not dublicated_files:
        print('\nNo dublicated files have been found in this directory tree.')
    else:
        print('\nThe following files are dublicates: \n')
        for dubl_file in dublicated_files:
            print('Location: {}\tFile: {}'.format(dubl_file[0], dubl_file[1]))

def main():
    dirpath = create_parser()
    if os.path.exists(dirpath.path_to_dir):
        all_files_in_tree = get_files_list(dirpath.path_to_dir)
        dublicated_files = find_dublicates(all_files_in_tree)
        print_results(dublicated_files)
=======

    parser = argparse.ArgumentParser(prog = 'Search for duplicates',
                                     description = '''The script searches for dublicated files
in current working directory or any other directory (need to specify its absolute path). ''',
                                     epilog = '''(c) p-well 2017. The author of the program 
does not bear any responsibility.''')

    parser.add_argument('path_to_dir', nargs='?', default = current_dir_path)
    parsed_dirpath = parser.parse_args()
    return parsed_dirpath
	
if __name__ == '__main__':

    current_dir_path = os.getcwd() 
    parsed_dirpath = create_parser()

    if not os.path.isdir(parsed_dirpath.path_to_dir):

        print('\nNo such directory, check path and try again')

>>>>>>> b01ec102e7eec5ecdb4aaf0ad0c2fd9d65200ca0
    else:  
        print('\nInvalid path, try again')        

<<<<<<< HEAD
if __name__ == '__main__':
    main()
=======
        all_files_in_tree = get_files_list(parsed_dirpath.path_to_dir)
        dublicated_files = find_dublicates(all_files_in_tree)
        
        if not dublicated_files:
            print('\nNo dublicated files have been found in this directory tree.')
        else:
            print('\nThe following files are dublicates: \n')
            for dubl_file in dublicated_files:
                print('Location: {}\tFile: {}'.format(dubl_file[0], dubl_file[1]))
>>>>>>> b01ec102e7eec5ecdb4aaf0ad0c2fd9d65200ca0
