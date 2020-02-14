#邀请我喜欢的人
giant_humans=['Albert Einstein','Max Planck','Dirac']
print(giant_humans[0:2])
for hum_name in giant_humans:
    print(hum_name)
print('I want to invite '+giant_humans[0]+' to my party!')
print('I want to invite '+giant_humans[1]+' to my party!')
print('I want to invite '+giant_humans[2]+' to my party!')
print(giant_humans[2]+" can not come for some stuffs.")
giant_humans[2]='Young'
for hum_name in giant_humans:
    print('I want to invite '+hum_name+' to my party!')
print("Oh!I find a bigger table,I would invite more giants.")
giant_humans.insert(0,'Bohr')
giant_humans.insert(2,'Heisenberg')
giant_humans.append('Veltman')
for hum_name in giant_humans:
    print('I want to invite '+hum_name+' to my party!')
print('I only can invite two guests,sorry for you!')
length=len(giant_humans)
print("Sorry!"+giant_humans.pop())
print("Sorry!"+giant_humans.pop())
print("Sorry!"+giant_humans.pop())
print("Sorry!"+giant_humans.pop())
print("Congratulations! "+giant_humans[0],'and '+giant_humans[1]+',we will have a good time!')
del giant_humans[0]
del giant_humans[0]
print(giant_humans)
print(length)