from pathlib import Path
import os



print('TB TAG manager || By the IT guy')

appdata = os.getenv('APPDATA')
tbpath = os.path.join(appdata, 'Thunderbird','Profiles')

dir = os.listdir(tbpath)
dir = list(dir)



print('Dirs disponibles:')
for index, item in enumerate(dir, 1):
    print(f"{index}. {item}")

seleccion = int(input("Introduce the number: ")) - 1


if 0 <= seleccion < len(dir):
    seleccionado = dir[seleccion]
    print(f"Has seleccionado: {seleccionado}")
else:
    print('No válida')


txt = Path(__file__).parent / 'etiquetas.txt'

js = os.path.join(tbpath, seleccionado, 'prefs.js')


def etiquetas(og,copia): 
	with open(og, 'r', encoding='utf-8') as start:
		cosas = start.read()


	with open(copia, 'a', encoding='utf-8') as end:
		end.write('\n')
		end.write(cosas)



etiquetas(txt,js)
