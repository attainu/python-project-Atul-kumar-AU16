import os
import shutil
import os.path
import time

from datetime import datetime

# this function is used to know the size
def size():

    path = input("enter your directory path:-")
    size = 0
    fsizedicr = {'Megabytes': float(
        1)/(1024*1024)}
    for (path, dirs, files) in os.walk(path):
        for file in files:
            filename = os.path.join(path, file)
            size += os.path.getsize(filename)
    for key in fsizedicr:
        if(key == "Megabytes"):
            print("Folder Size: " + str(round(fsizedicr[key]*size, 2)) + " MB")


print("""Type byext to organize by their extension
        Type bydate to organize by their date
        Type fsize to know file size""")


op = input("ENTER YOUR OPTION:-")

if op == "fsize":
    size()

elif op == "bydate":
    bydate()

