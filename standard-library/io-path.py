# Go through all files under ./directory
import os
directory = './directory'
start = None
end = None
for filename in list(os.listdir(directory))[start:end]:
    route = os.path.join(directory, filename)
    if filename.endswith(".txt"): 
        print(filename)
    elif os.path.isdir(route):
        print(filename, 'dir')
    else:
        print(filename, 'other file')

# the directory of the script being run:
import os
os.path.dirname(os.path.abspath(__file__))

# the current working directory:
os.getcwd()
