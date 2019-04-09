# Author: Victor Ding

# with open("file.txt","r") as fh:
#     for line in fh:
#         print(line.strip())
#     fh.close()

# with open("file.txt","r") as fh:
#     for line in fh.readlines():
#         print(line.strip())
#     fh.close()

# with open("file.txt","r+") as fh:
#     fh.write("TITLE\n")
#     l = fh.readlines().copy()
#     l.reverse()
#     for line in l:
#         fh.write(line)
#     fh.write("THE END")

with open("file.txt","a+") as fh:
    fh.seek(0)  # 挪动光标，好像只对read有效
    l = fh.readlines().copy()
    l.reverse()
    for line in l:
        fh.write(line)
    fh.write("THE END")
    fh.close()

with open("file.txt","r") as fh:
    for line in fh:
        print(line)
    fh.close()

