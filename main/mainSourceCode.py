# Junk file organizer
import os
import shutil
import os.path
import time
import math

from datetime import datetime

# this function is used to sort files by extension


def bytype(): 

    path = input("enter path directory :-")

    lis = os.listdir(path)
    lis.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime)

    # List only the files in the folder
    # change the current path

    os.chdir(path)

    arr = os.listdir()

    slash = "\\"

    file_types = {

        "Text": [".doc", ".rtf", ".txt", ".wps", ".docx"],
        "Data": [".csv", ".pps", ".ppt", ".pptx", ".xml"],
        "Music": [".mp3", ".m4a", ".m4a",  ".m4p", ".mp3", "ogg"],
        "Video": [".3gp", ".avi", ".flv", ".m4v", ".mov", ".mp4", ".wmv"],
        "notes": [".pdf"],
        "Spreadsheet": [".xlr", ".xls", ".xlsx"],
        "apps": [".apk", ".app", ".exe", ".jar"],
        "Web": [".css", ".htm", ".html", ".js", ".php", ".xhtml"],
        "Compressed": [".rar", ".zip"],
        "Programmes": [".c", ".class", ".cpp", ".cs", ".java", ".py"],
        "Misc": [".ics", ".msi", ".torrent"],
        "images": [".jpeg", ".png", ".jpg"]
    }

    for x in arr:
        fflag = 0
        if os.path.isfile(x):
            if("." in x):
                extension_name = x[x.index("."):]
                for file_type, extensions in file_types.items():
                    if extension_name in extensions:
                        fflag = 1
                        folder_name = file_type
                        newpath = path + slash + folder_name
                        #print(newpath)
                        break
                if (fflag == 0):
                    folder_name = "Other"
                    newpath = path + slash + folder_name
                    #print(newpath)
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            shutil.move(path + slash + x, newpath + slash + x)


# this function is used to sort by date

def bydate():

    path = input("enter path directory :-")
    lis = os.listdir(path)
    lis.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime)
    files = [f for f in os.listdir(
        path) if os.path.isfile(os.path.join(path, f))]
    os.chdir(path)

    for x in files:

        # Get the last modified time and the creation time

        modified_time_string = time.ctime(
            os.path.getmtime(os.path.join(path, x)))

        modified_datetime_obj = datetime.strptime(
         modified_time_string, '%a %b %d %H:%M:%S %Y')

        modified_date = str(modified_datetime_obj.day) + '-' + str(
         modified_datetime_obj.month) + '-' + str(modified_datetime_obj.year)

        if(os.path.isdir(modified_date)):
            shutil.move(os.path.join(path, x), modified_date)
        else:
            os.makedirs(modified_date)
            shutil.move(os.path.join(path, x), modified_date)


# this function is used to know the size
def organizeBySize():
    path=input("Enter the path:")
    dirs=os.listdir(path)
    dir_size1={}

    for j in dirs:
        dir_size1[j]=os.stat(os.path.join(path,j)).st_size

    sorted_dir=sorted(dir_size1.items(),key=lambda c:c[1])
    dir_size0 = []
    size_types = []

    for j in sorted_dir:
        a1 = (os.stat(os.path.join(path,j[0])).st_size)
        a2 = convert_size(a1)
        a3 = str(a2).split("_")

        if a3 == [] or a3 == ["0B"]:
            pass
        else:
            dir_size0.append(a3)
    types=[]
    sub = "."
    for j in sorted_dir:
        if sub in j[0]:
            b1=j[0][::-1].find(".")
            b2=j[0][-b1:]
        if b2 not in types:
            types.append(b2)

    #creating folder
    for j in dir_size0:
        if j[1] not in size_types:
            size_types.append(j[1])
    for j in size_types:
        for k in dir_size0:
            if k[1] == j and int(k[0]) < 50 :
                if not os.path.exists(os.path.join(path,"Less Than 50" + k[1])):
                    os.mkdir(os.path.join(path,"Less Than 50"+k[1]))
            elif k[1] == j and int(k[0]) > 50:
                if not os.path.exists(os.path.join(path,"Grater Than 100" + k[1])):
                    os.mkdir(os.path.join(path,"Grater Than 100" + k[1]))

    #moving files to folder
    newFiles = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path,file))]
    x = [x for x in newFiles if checkFIle(x) == False]
    for j in x:
        new_size = convert_size(os.stat(os.path.join(path,j)).st_size)
        new_size = new_size.split("_")
        if int(new_size[0]) < 50 :
            shutil.move(os.path.join(path,j),os.path.join(path,"Less Than 50" + new_size[1]))
        else:
            shutil.move(os.path.join(path,j),os.path.join(path,"Grater Than 100" + new_size[1]))

    # converting bytes to readable size
def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"

    size_name=("B","KB","MB","GB","TB","PB","EB","ZB","YB")
    i=int(math.floor(math.log(size_bytes,1024)))
    p=math.pow(1024,i)
    s=round(size_bytes/p,2)
    return "%s_%s" % (round(s),size_name[i])

def checkFIle(fileName):
    d = os.path.basename(__file__)
    if fileName == d:
        return True
    return False

if __name__ == "__main__":


    print("""           Type "bytype" to organize by their extension
            Type "bydate" to organize by their date
             Type "size" to know file size""")


    op = input("ENTER YOUR OPTION:-")

    if op == "bytype":
        #print("ORGANISED")
        bytype()
        print("ORGANISED by extension")

    elif op == "bydate":
        bydate()
        print("ORGANISED by date")

    elif op == "size":
        organizeBySize()
        print("ORGANISED by size")

        