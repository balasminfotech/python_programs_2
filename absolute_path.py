import os
print(os.path.abspath(__file__))
print(os.path.dirname(__file__))
sp=os.path.abspath(__file__)
srr=sp.split("\\")
print(srr[-1])

import os.path, time
# print("Last modified: %s" % time.ctime(os.path.getmtime("absolute_path.py")))
# print("Created: %s" % time.ctime(os.path.getctime("absolute_path.py")))