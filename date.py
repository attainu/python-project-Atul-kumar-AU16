# Junk file organizer
import os
import shutil
import os.path
import time


from datetime import datetime


print("WELCOME TO JUNK FILE ORGANISER")
print("PROGRAME BY - ATUL KUMAR")
print("FEATURES")


# this function is used to sort by date py

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

if __name__ == "__main__":


    print("""           Type "bytype" to organize by their extension
            Type "bydate" to organize by their date
             Type "size" to know file size""")


    op = input("ENTER YOUR OPTION:-")

    if op == "bytype":
        # print("ORGANISED")
        bytype()
        print("ORGANISED by extension")

    elif op == "bydate":
        bydate()
        print("ORGANISED by date")

    elif op == "size":
        organizeBySize()
        print("ORGANISED by size")
        