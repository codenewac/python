country_rivers={'nile':'egypt','Amazon River':'Columbia','Yangtse River':'China'}
for river in country_rivers.keys():
    print("The "+river.title()+" runs through ",country_rivers[river].title()+'.')
for river in country_rivers.keys():
    print(river.title())
for river,nation in country_rivers.items():
    print(nation.title())
for river in country_rivers.keys():
    print(country_rivers[river].title())
nile='nile'
country_rivers={nile:'egypt','Amazon River':'Columbia','Yangtse River':'China'}
country_rivers[nile]='egypts'
print(country_rivers)