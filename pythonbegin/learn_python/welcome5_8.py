clerks=[]
if clerks!=True:
    print("We need some users")
else:
    for clerk in clerks:
        if clerk == 'admin':
            print("Hello admin,would you like to see a status report?")
        else:
            print("Hello Eric,thank you for logging in again.")
