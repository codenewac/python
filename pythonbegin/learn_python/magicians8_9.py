magicians_name=['cady','bob','mack','penny','tiara']
def show_magicians(magicians):
    """打印魔术师的名字"""
    for magician in magicians:
        print("Hello! " + magician.title())
def make_magicians(magicians):
    """对魔术师列表修改"""
    for number in range(5):
        magicians[number]='the Great '+magicians[number]
    return magicians
magicians_name_copy=make_magicians(magicians_name[:])
show_magicians(magicians_name)
show_magicians(magicians_name_copy)