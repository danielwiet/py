import os
import subprocess as sp

path = input('Enter the path to the parent directory. (Sample location: /Users/mymacname/Desktop/ParentDirectory) \n')

dirs = [dir for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))]

print(dirs, end='\n')

sp.run(['cd ' + path, 'zip -r  lpbf.zip lpbf'], shell=True)