""" This script will zip all files and folders in a directory individually (option 0) or together (option 1).

File names must not contain spaces, or else this will not work

The path to the parent directory is required. On Windows computers, copy from the file explorer. For Macs, locate the directory in Finder, right click (ctr + click) on the directory, press and hold the option button to display the hidden option to copy path name. """


import os
import subprocess as sp
# above packages included in current release of python

print("What type of compression do you want? \n0. Each folder compressed separately \n1. All folders and files in one folder")
choice = input("Enter the number 0 or 1\n")
# If 0, all folders in the parent directory will be separate zipped files
# If 1, all folders and files in the parent directory will be zipped to one file

path = input('Enter the path to the parent directory. (Sample location: /Users/mymacname/Desktop/ParentDirectory) \n')
# inputs to the parent directory containing folders to compress
# on mac, right click on parent directory, then press the 'option' key to access hidden options. click 'copy (folder name) as pathname'

if choice == "0":

    dirs = [dir for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))]
    # creates a list of folders and files in the path directory

    """
    To do: input to include all files and folders Y/N
    If Y, proceed with zipping
    If N, regex folder/file search to only include desired parameters
    OR
    Create database to include all data, perform selection on the database and export to directory, then run the compression script
    """

    # print(dirs, end='\n')

    for dir in dirs:
        dir_path = path + '/' + dir
        dir_path_zip = dir_path + '.zip'
        # for each occurance in the dirs list, it will add the name at the end of the parent directory and save it with the '.zip' extension

        # print(dir_path, end='\n')
        # print(dir_path_zip, end='\n')
       

        terminal = ['cd ' + path + '\n' + 'zip -r ' + dir_path_zip + ' ./' + dir]
        # this is the script that will tell the terminal what to do. For each loop it will navigate to the parent directory (path), runs the command 'zip -r', and saves it in the parent directory

        # terminal command % zip -r archive_name.zip(dir_path_zip) folder_to_compress(dir)

        sp.run(terminal, shell=True)
        # This runs the subprocess that will write the compressed files to the parent directory

        # print(dirs, end='\n')

elif choice == "1":

    path_zip = path + '.zip'

    terminal = ['cd ' + path + '\n' + 'zip -r ' + path_zip + ' ./']

    sp.run(terminal, shell=True)