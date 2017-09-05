# Anti-Duplicator

The purpose of the script it to find duplicated files in directory tree - files with the same name and size.
The script searches for doubles and prints dublicate's path and name.

# Quickstart

Python 3.5 should be already installed.

To run the script execute ```python duplicates.py <filepath>``` in CLI. The script will recursively check all files in current directory tree.

# Example of Script Launch

```
c:\projects\devman\11_duplicates>python duplicates.py C:\projects\1_test_folder

The following files are dublicates:

Location: C:\projects\1_test_folder\sub1        File: file1.txt
Location: C:\projects\1_test_folder\sub2        File: file20.txt
Location: C:\projects\1_test_folder\sub3        File: file2.txt
```

Running with wrong path:

```
c:\projects\devman\11_duplicates>python duplicates.py C:\projects\1_test_fold

Invalid path, try again
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
