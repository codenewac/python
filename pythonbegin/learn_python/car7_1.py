prompt="What kind of car do you want to lend"
temp=input(prompt)
print(temp.title()+"?Let me see if I can find you a Subaru")
number=input("How many people would for dinner?")
number=int(number)
if number >= 8:
    print("No free table!")
else:
    print("Enough")
number_1=input("Input a number.")
number_1=int(number_1)
if number_1%10==0:
    print("YES")
else:
    print("No!")