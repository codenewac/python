"""name=input("Please input your name ")
filename='guest.txt'
with open(filename,'w') as file_object:
    file_object.write(name)"""
while True:
    filename_1='guest_book.txt'
    name_1=input("please input your name ")
    print("Welcome to our game!\nAnytime you want to exit,please input 'p'")
    if name_1!='p':
        with open(filename_1,'a') as file_object:
            file_object.write(name_1.title()+'\n')
    else:
        break