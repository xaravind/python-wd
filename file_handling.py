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