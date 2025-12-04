fh = open("args.py")

content = fh.read()

print("The content of file is :", content )


# line = fh.readline()

for  i in range(10):
    line = fh.readline()
    print(line, end="")


fh.close()