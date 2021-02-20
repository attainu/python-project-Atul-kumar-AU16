------------------------------------JUNK FILE ORGANISER----------------------------------------------------

This might seem very useful for a lazy python programmer who keeps most of the files and folders at 
one location and sometimes at confused what all files are there and surely he is too lazy to do it 
manually. So below is a python program to organize or simplify everything in appropriate folder in 
the single go and remove empty directories.

What do it do…?

   1.Organize by extension
   2.Organize by size
   3.Organize by Number of days
   4.Organize by total folder size


What happens inside….?

Whenever the user selects the option,the files will be organised based on the option selected by the user.
 Below are the given scenarios for which how they organise like:-

• Organise by extension:- 
   By using this option user can organize their files by their file extension in a given folder, folder 
   will be created according to file extension and finally all files will be moved to a created folder.

• Organise by size:- By using this option user can organize their files by their file size, according to
  file sizes random folders will be created and respective files will be moved to them.

• Organise by Last used/accessed date:- By using this option user can organize their files by last used
   date. random folders will be created according to files last used date and files will be moved to them.

• Organize by total folder size:- By using this option user can know their file size in a particular folder.
  


At a glance:-

• I had used Shutil/Os modules for the file arrangement.

• Dateandtime to know when the files were created and many more built-in functions.

• I have a directory path where lots of files of different types are present (like above) and my program
  segregate each file type into their respective folders.

 • As a future scope of this project,We can design the ui for the program so that a normal user can 
   easily interact with it. We can add more features like deleting the junk files after a certain period 
   of time.  
