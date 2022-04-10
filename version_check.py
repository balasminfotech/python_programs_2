import platform
import os

print("\n OS Name :",os.name)
print("\n system :",platform.system())
print("\n machine :",platform.machine())
print("\n architecture :",platform.architecture())
print("\n release :",platform.release())


import site; 
print(site.getsitepackages())
print(os.path.realpath(__file__))
import multiprocessing
print(multiprocessing.cpu_count())
print(os.path.realpath(__file__))