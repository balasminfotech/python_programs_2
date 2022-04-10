# ext=input("Enter the file name with extension : ")
# values = ext.split(".")
# print(values[-1])

# n=input("entern value")
# n1=int("%s" % n)
# n2=int("%s%s" % (n,n))
# n3=int("%s%s%s" % (n,n,n))
# print(n1+n2+n3)


import os
 
# Get the list of all files and directories
# path = "E:/webApplication/Projects_1/"
# dir_list = os.listdir(path)
 
# print("Files and directories in '", path, "' :")
 
# prints all files
# print(dir_list)

for x in os.listdir():
    if x.endswith(".py"):
        # Prints only text file present in My Folder
        print(x)