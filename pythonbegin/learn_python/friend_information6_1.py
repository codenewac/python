friend_information={'first_name':'albert','last_name':'einstein','age':34,'city':'Switzerland'}
friend_information_1={'first_name':'max',"last_name":'planck','age':45,'city':'berlin'}
friend_infos=[friend_information_1,friend_information]
for friend_info in friend_infos:
    for key,value in friend_info.items():
        print(str(value).title())
print(friend_information['first_name'].title())
print(friend_information['last_name'])
print(friend_information['age'])
print(friend_information['city'])
friend_number={
    'friend_a':1,
    'friend_b':2,
    'friend_c':3,
    'friend_d':4,
    'friend_e':5,
    }
print(friend_number['friend_a'])
name='Eric'
print(name)