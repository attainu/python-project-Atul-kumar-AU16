# Junk file organizer
import os
import shutil
import os.path
import time
import math

print("WELCOME TO JUNK FILE ORGANISER")
print("PROGRAME BY - ATUL KUMAR")
print("FEATURES")

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


    print("""  
            Type "size" to know file size         
                
                """)


    op = input("ENTER YOUR OPTION:-")

    if op == "size":
        organizeBySize()
        print("ORGANISED by size")

    elif op == "bydate":
        bydate()
        print("ORGANISED by date")

    

