import sys
import os
 
if len(sys.argv) != 2:
    print("Usage: python file_checker.py <file_path>")
    sys.exit(1)
 
file_path = sys.argv[1]
 
if os.path.exists(file_path):
    print(f"The path {file_path} exists!")
 
    if os.path.isfile(file_path):
        print("It is a file")
    elif os.path.isdir(file_path):
        print("It is a directory")
   
else:
    print(f"The path {file_path} does not exist")