import os
print(os.path.basename("E:\webApplication\Projects_1\get_filename.py"))
print(os.path.dirname("E:\webApplication\Projects_1\get_filename.py"))

x="E:\webApplication\Projects_1\get_filename.py"
r=x.split("\\",-1)
# print(r)
print(r[-1])
