import tkinter as tk
from tkinter import messagebox
from pathlib import Path
import os
import re


# Función para añadir nuevas etiquetas
def newtag():
    hexcol = entry_color.get()
    newtag = entry_tittle.get()

    if not hexcol.startswith("#") or len(hexcol) != 7:
        messagebox.showerror("Error", "Non valid hexcode  (Ref: #d042e3).")
        return
    
    if not newtag:
        messagebox.showerror("Error", "Avoid empty boxes.")
        return

    tags = "etiquetas.txt" # Change 
    
    with open(tags, "r") as f:
        lines = f.readlines()

    numtag = sum(1 for line in lines if 'mailnews.tags.$label' in line and '.color' in line)
    sumtag = numtag + 1

    new_line_color = f'user_pref("mailnews.tags.$label{sumtag}.color", "{hexcol}");\n'
    new_line_tag = f'user_pref("mailnews.tags.$label{sumtag}.tag", "{newtag}");\n'

    with open(tags, "a") as f:
        f.write(new_line_color)
        f.write(new_line_tag)

    messagebox.showinfo("Success", f"Label{sumtag} has been added successfully as {newtag}.")

def apply_tags():

    appdata = os.getenv('APPDATA')
    tbpath = os.path.join(appdata, 'Thunderbird', 'Profiles')

    dir = os.listdir(tbpath)
    dir = list(dir)

    # Find the longest option or the one matching the pattern *.*-*
    pattern = re.compile(r'.*\..*-.*')
    longest_option = max(dir, key=len)
    pattern_option = next((item for item in dir if pattern.match(item)), None)

    if pattern_option:
        choice = pattern_option
    else:
        choice = longest_option


    txt = Path(__file__).parent / 'etiquetas.txt'
    js = os.path.join(tbpath, choice, 'prefs.js')

    with open(txt, 'r', encoding='utf-8') as start:
            opog = start.read()


    with open(js, 'a', encoding='utf-8') as end:
            end.write('\n')
            end.write(opog)
		


def tag_editor():
    # Crear una nueva ventana
    editor_window = tk.Toplevel(root)
    editor_window.title("Gestionar Etiquetas")
    editor_window.geometry("400x200")

    global entry_color, entry_tittle  # Definimos las entradas como globales para que sean accesibles en newtag

    # Nueva etiqueta de color hexadecimal
    label_color = tk.Label(editor_window, text="Hex color (#d042e3):")
    label_color.pack(pady=5)
    entry_color = tk.Entry(editor_window)
    entry_color.pack(pady=5)

    # Nueva etiqueta de título
    label_tittle = tk.Label(editor_window, text="Tag title (1. ANY):")
    label_tittle.pack(pady=5)
    entry_tittle = tk.Entry(editor_window)
    entry_tittle.pack(pady=5)

    # Botón para añadir la nueva etiqueta
    

    createrbtn = tk.Button(editor_window, text="Add new tag", command=newtag)
    createrbtn.pack(pady=20)

    close_button = tk.button(editor_window, text="Close", command=editor_window.destroy)
    close_button.pack(pady=10)

    # Botón para cerrar la ventana emergente
    

# Función para aplicar etiquetas (la puedes definir según lo que desees que haga)
def aplicar_etiquetas():
    aplicar_window = tk.Toplevel(root)
    aplicar_window.title("Aplicar Etiquetas")
    aplicar_window.geometry("400x200")
    label = tk.Label(aplicar_window, text="Aquí se aplicarán las etiquetas.")
    label.pack(pady=20)


# Crear la ventana principal con los botones
root = tk.Tk()
root.title("TBTM - Main Menu")
root.geometry("400x200")

btn_aplicar = tk.Button(root, text="Aplicar etiquetas", command=apply_tags)
btn_aplicar.pack(pady=10)

btn_gestionar = tk.Button(root, text="Gestionar etiquetas", command=tag_editor)
btn_gestionar.pack(pady=10)

root.mainloop()
