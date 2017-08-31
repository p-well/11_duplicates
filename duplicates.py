import os

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
	
if __name__ == '__main__':
    
    all_files_in_tree = get_files_list('C:\projects\ptest_folder')
    dublicated_files = find_dublicates(all_files_in_tree)
	
    if len(dublicated_files) == 0:
        print('No dublicated files have been found in this directory tree.')
    else:
        print('\nThe following files are dublicates: \n')
        for dubl_file in dublicated_files:
            print('Location:{}\tFile:{}'.format(dubl_file[0], dubl_file[1]))
