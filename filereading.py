file_read = open('file.txt', 'r')

print("The whole thing")
print(file_read.read())

print("7 letters")
print(file_read.read(7))

print("3 lines")
print(file_read.readline())
print(file_read.readline())
print(file_read.readline())

file_read.close()