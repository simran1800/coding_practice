# soldier function takes three arguments.
# The first argument is path of the directory that needs to be prettified(capitalise the firdt letter of the name of files.
# Second arguement is path of the file that has names of files as exceptions( keep unchanged).
# Third argument has format of the file that has to be numbered.

import os
def soldier(path, file, format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")
        # print(filelist)

    for file in files:
        if file.split(".")[0] not in filelist:
            # print(file)
            os.rename(file, file.capitalize())

            if os.path.splitext(file)[1] == format:
                os.rename(file, f"{i}{format}")
                i +=1


p=input("Enter the path of the folder that needs to be prettified: ")
f=input("Enter the path of the file that contains the names of exception files: ")
n=input("Enter the format that needs to be numbered in ascending order(.jpg): ")

soldier(p,f,n)