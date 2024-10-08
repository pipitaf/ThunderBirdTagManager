import os
import re
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, OptionMenu, StringVar



def terminate():
    os.system('taskkill /IM "' + "thunderbird.exe" + '" /F')

terminate()



def newtag(editor_window):

    tags = text_file

    hexcol = entry_color.get()
    newtag = entry_tittle.get()

    if not hexcol.startswith("#") or len(hexcol) != 7:
        messagebox.showerror("Error", "Non valid hexcode  (Ref: #d042e3).")
        return

    if not newtag:
        messagebox.showerror("Error", "Avoid empty boxes.")
        return



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

    editor_window.destroy()

def apply_tags():
    appdata = os.getenv('APPDATA')
    tbpath = os.path.join(appdata, 'Thunderbird', 'Profiles')

    dir = os.listdir(tbpath)
    dir = list(dir)

    # Longest or matching pattern

    pattern = re.compile(r'.*\..*-.*')
    longest_option = max(dir, key=len)
    pattern_option = next((item for item in dir if pattern.match(item)), None)

    if pattern_option:
        choice = pattern_option
    else:
        choice = longest_option

    txt = Path(__file__).parent / text_file
    js = os.path.join(tbpath, choice, 'prefs.js')

    with open(txt, 'r', encoding='utf-8') as start:
        opog = start.read()

    with open(js, 'a', encoding='utf-8') as end:
        end.write('\n')
        end.write(opog)

def tag_editor():
    editor_window = tk.Toplevel(root)
    editor_window.title("Manage tags")
    editor_window.geometry("400x300")

    global entry_color, entry_tittle, option

    label_team = tk.Label(editor_window, text=f"Currently you're in {option}")
    label_team.pack(pady=10)

    # Hex
    label_color = tk.Label(editor_window, text="Hex color (#d042e3):")
    label_color.pack(pady=5)
    entry_color = tk.Entry(editor_window)
    entry_color.pack(pady=5)

    # Tag
    label_tittle = tk.Label(editor_window, text="Tag title (1. ANY):")
    label_tittle.pack(pady=5)
    entry_tittle = tk.Entry(editor_window)
    entry_tittle.pack(pady=5)

    createrbtn = tk.Button(editor_window, text="Add new tag", command=lambda: newtag(editor_window))
    createrbtn.pack(pady=20)



# ROOT

root = tk.Tk()
root.title("TBTM - Main Menu")
root.geometry("400x200")

btn_apply = tk.Button(root, text="Apply tag", command=apply_tags)
btn_apply.pack(pady=10)

btn_manage = tk.Button(root, text="Manage tags", command=tag_editor)
btn_manage.pack(pady=10)

# team selector

selected_option= StringVar(root)

selected_option.set("Current team")

teams = ["Admon","Produccion","Support"]

basepath= "EQUIPOS"



team_paths = {
    "Admon":os.path.join(basepath, "tagAdm.txt"),
    "Produccion": os.path.join(basepath, "tagProd.txt"),
    "Support": os.path.join(basepath,"tagSupp.txt")
}

text_file = "" # <-- change this | If you have many teams ignore and change var "teams"

def sel_teams(*args):
    global text_file
    global option
    option = selected_option.get()
    text_file = team_paths.get(option,"")



drop_menu = OptionMenu(root, selected_option,*teams)
drop_menu.pack(pady=10)

selected_option.trace("w", sel_teams)



root.mainloop()

