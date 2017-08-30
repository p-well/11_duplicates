import os

def get_files_list(folderpath):
    files_list = []
    for dirpath, subdirs, files in os.walk(folderpath):
        for file in files:
            filepath = os.path.join(dirpath, file)
            filesize = os.path.getsize(filepath)
            files_list.append((dirpath, file, filesize))
    print(files_list)

def find_dublicates(files_list):
    dublicated_files = []
    non_dublicated_files = []


if __name__ == '__main__':
    all_files_in_tree = get_files_list('C:\projects\ptest_folder')
