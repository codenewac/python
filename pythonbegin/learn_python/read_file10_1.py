filename='learning_python.txt'
with open(filename) as file_object:
    contents=file_object.read()
    print(contents)
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())
with open(filename) as file_object:
    lines=file_object.readlines()
for line in lines[:3]:
    line=line.replace('Python','Java')
    print(line.rstrip())
line_1="python java"
line_2=line_1.replace('java','cpp')
print(line_1,line_2)