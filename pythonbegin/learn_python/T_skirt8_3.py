def describe_pet(pet_name,animal_type=' '):
    """显示宠物信息"""
    print("I have a "+animal_type)
    print("My pet name is "+pet_name.title())
describe_pet('tom','cat')
def make_album(singer_name,album_name,album_num=''):
    """创建描述音乐的字典"""
    if album_num:
        album = {"singer": singer_name, 'album': album_name,'album_number':album_num}
        return album
    else:
        album = {"singer": singer_name, 'album': album_name}
        return album
album_1=make_album('singer_a','album_a')
print(album_1)
while True:
    print("\nPlease input singer.")
    print("(enter 'q' any time to quit.)")
    singer_A=input("Please input singer name ")
    if singer_A=='q':
        break
    singer_album=input('Please input singer album ')
    if singer_album=='q':
        break
    album_2=make_album(singer_A,singer_album)
    print(album_2)