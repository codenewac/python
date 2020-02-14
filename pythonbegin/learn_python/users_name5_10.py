current_users=['user_1','user_2','User_3','uSer_4',"USER_5"]
new_users=['user_a','user_3',"user_b",'user_5','user_c']
current_users_1=[]
for current_user_1 in current_users:
    current_users_1.append(current_user_1.lower())
print(current_users_1)
for new_user in new_users:
    if new_user.lower() in current_users_1:
        print(new_user.title()+",this name was used.")
    else:
        print(new_user.title()+",this name was a new name.")
numbers=list(range(1,10))
for number in numbers:
    if number <= 1:
        print('1st')
    elif number<=2:
        print("2nd")
    elif number<=3:
        print('3rd')
    else:
        print(str(number)+'th')