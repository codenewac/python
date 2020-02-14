favorite_places={
    'newton':['beijing','paris','london'],
    'bohr':['shanghai','berlin','newyork'],
    'enstein':['Munich','Switzerland','beijing']
}
for name,favorite_place in favorite_places.items():
    print('\n'+name.title()+' love these cities:')
    for favorite_place_1 in favorite_place:
        print("\t"+favorite_place_1.title())
print("I love you baby")