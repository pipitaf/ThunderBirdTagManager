import tkinter as tk
from tkinter import messagebox



def newtag():
    hexcol = entry_color.get()
    newtag = entry_tittle.get()

    if not hexcol.startswith("#") or len(hexcol) != 7:
        messagebox.showerror("Error", "Non valid code (ej: #d042e3).")
        return
    
    if not newtag:
        messagebox.showerror("Error", "Avoid empty tag.")
        return

    tags = "etiquetas.txt"
    
    
    with open(tags, "r") as f:
        lines = f.readlines()

    numtag = sum(1 for line in lines if 'mailnews.tags.$label' in line and '.color' in line)
    sumtag = numtag + 1

    new_line_color = f'user_pref("mailnews.tags.$label{sumtag}.color", "{hexcol}");\n'
    new_line_tag = f'user_pref("mailnews.tags.$label{sumtag}.tag", "{newtag}");\n'

    with open(tags, "a") as f:
        f.write(new_line_color)
        f.write(new_line_tag)

    messagebox.showinfo("Success", f"Label{sumtag} has been added succesfully as {newtag}.")
    
    # Limpiar los campos de entrada
    entry_color.delete(0, tk.END)
    entry_tittle.delete(0, tk.END)

    return(tags)


tags = "etiquetas.txt"

window = tk.Tk()
window.title("TBTM")
window.geometry("400x200")

#New hex
label_color = tk.Label(window, text="Hex color (#d042e3):")
label_color.pack(pady=5)
entry_color = tk.Entry(window)
entry_color.pack(pady=5)

#New tags
label_tittle = tk.Label(window, text="Tag tittle (1. ANY):")
label_tittle.pack(pady=5)
entry_tittle = tk.Entry(window)
entry_tittle.pack(pady=5)

createrbtn = tk.Button(window, text=f"Add new tag to {tags}", command=newtag)
createrbtn.pack(pady=20)

window.mainloop()
