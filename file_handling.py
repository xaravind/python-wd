fh = open("args.py")

content = fh.read()

print("The content of file is :", content )


# line = fh.readline()

for  i in range(10):
    line = fh.readline()
    print(line, end="")

# for line in fh.readlines():
#    print(line)

fh.close()


with open("args.py") as fh:
    for line in fh.readlines():
        print(line)

# best method , it auto closes..

with open("args.py", "r") as fh:
    for line in fh.readlines():
        print(line)
# it set the mode like read add r


try:
    with open("args.py", "r") as fh:
        for line in fh.readlines():
            print(line)
except  FileNotFoundError:
    print("File not found")
else:
    print("try-except block")
finally:
    print("will get excuted")

    

# graceful error handeling

# if you want to pass absolute path of file

# use raw string r"path"

#r"C:\Users\KR757CV\OneDrive - EY\Desktop\GenAI\Regression.py" or

# C:\\Users\\KR757CV\OneDrive - EY\Desktop\GenAI\Regression.py (replace \ with \\)

# w mode will rewrite the content in file
# fh.write("content")


# x for creating and writing to a new file
# a for append at the end of file (it also create a file if file not exist)

# we can have multi except statements


# try:
#     with open(r"C:\Users\VishwasKSingh\Workspace\ey-wd-workspace\test2.txt","a") as fh:
#         fh.write("I am vishwas k singh")
 
#     # print("The content of the file is: ", line)
#     print("\nthe conent of the file has ended")
# except FileNotFoundError:
#     print("File you are trying to open does not exist")
# except FileExistsError:
#     print("File that you are tring to write already exists")
# else:
#     print("This is an else block for try-except")
# finally:
#     print("Will always be executed")
 
 