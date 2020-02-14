favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
research_list=['jen','phil','james','tom']
for human in research_list:
    if human in favorite_languages.keys():
        print(human.title()+",thanks for your cooperation!")
    else:
        print(human.title()+',could you please help me finish a research?')