from pathlib import Path
import os

# Get the base directory
basepath = Path()
print(basepath)

basedir = str(basepath.cwd())
print(basedir)

# Load the environment variables
envars = basepath.cwd() / '.env'
# print(dirname(__file__))