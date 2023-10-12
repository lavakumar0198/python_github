# file1 = open("demo1.txt",mode="r")
# # c = file1.read()
# # c = file1.read(4)
# # c = file1.readline()
# c = file1.readlines()
# print(c)
# file1.close()


# file1 = open("write.txt",mode="w")
# c = file1.write("this is write")
# file1.close()


# file1 = open("write.txt",mode="a")
# c = file1.write("this is append")
# file1.close()


# file1 = open("write.txt",mode="r+")
# print(file1.tell())
# print(file1.read())
# print(file1.tell())


# file1 = open("write.txt",mode="w+")
# print(file1.tell())
# c=file1.write("this is w+")
# print(file1.read())
# print(file1.tell())


# file1 = open("write.txt","r")
# print(file1.tell())
# file1.read(2)
# print(file1.tell())
# file1.seek(0)
# print(file1.tell())
# file1.close()


file = open("write.txt","r+")
content = file.read()
v = str(content)
print(v)
f = v.split()
print(f)
f.insert(2,"lava")
print(f)
print(file.tell())
file.close()
file = open("write.txt","w")
print(f)
for i in f:
    file.writelines([i])