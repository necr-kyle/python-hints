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
    elss:
        pritn(file, 'other file')
