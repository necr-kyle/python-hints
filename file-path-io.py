# Go through all files under ./directory
import os
directory='./directory'
start=None
end=None
for file in list(os.listdir(directory))[start:end]:
    route=os.path.join(directory,file)
    if file.endswith(".txt"): 
        print(file)
    elif os.path.isdir(route):
        print(file, 'dir')
    else:
        print(file, 'other file')

# the directory of the script being run:
import os
os.path.dirname(os.path.abspath(__file__))

# the current working directory:
os.getcwd()
