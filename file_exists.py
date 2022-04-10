import os
print(os.path.exists("concenate.py"))

print(os.path.isfile("concenate.py"))

myfile=open("concenate.py")
try:
    myfile.close()
    print("file exists")
except FileNotFoundError:
    print("File not found")


path = "E:/webApplication/Projects_1/for.py"
if os.path.isfile(path):
    print("File exists in path")
elif os.path.isdir(path):
    print("Directory exists in path")
else:
    print("File formats are different")