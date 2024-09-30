from pathlib import Path
import os



print('TB TAG manager || By Pipitaf')

appdata = os.getenv('APPDATA')
tbpath = os.path.join(appdata, 'Thunderbird','Profiles')

dir = os.listdir(tbpath)
dir = list(dir)



print('Avaliable dirs:')
for index, item in enumerate(dir, 1):
    print(f"{index}. {item}")

select = int(input("Select: ")) - 1


if 0 <= select < len(dir):
    choice = dir[select]
    print(f"You chosed: {choice}")
else:
    print("Choice wasn't valid")


txt = Path(__file__).parent / 'etiquetas.txt'

js = os.path.join(tbpath, choice, 'prefs.js')


def insert(og,copy): 
	with open(og, 'r', encoding='utf-8') as start:
		opog = start.read()


	with open(copy, 'a', encoding='utf-8') as end:
		end.write('\n')
		end.write(opog)



insert(txt,js)
