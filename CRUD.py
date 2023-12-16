import tkinter as tk
from tkinter import messagebox

def  create():
    item = item_entry.get()
    if item:
        items_listbox.insert(tk.END, item)
        item_entry.delete(0, tk.END)

def read():
    selected_item = items_listbox.curselection()
    if selected_item:
        item = items_listbox.get(selected_item)
        messagebox.showinfo('Selecionado', f'Dados - {item}')
   


def update():
    selected_item = items_listbox.curselection()
    if selected_item:
        new_item = item_entry.get()
        if new_item:
            items_listbox.delete(selected_item)
            items_listbox.insert(selected_item, new_item)
            item_entry.delete(0, tk.END)

def delete():
    selected_item = items_listbox.curselection()
    if selected_item:
        items_listbox.delete(selected_item)

root = tk.Tk()
root.title('CRUD')
root.geometry('400x400')



item_label = tk.Label(root, text= 'Digite o seu E- mail', font=('arial',25, 'bold'))
item_label.pack()
item_entry = tk.Entry(root, width=57)
item_entry.pack()

btn_create = tk.Button(root, text='Salvar', command=create, width=15)
btn_create.pack()

items_listbox = tk.Listbox(root, width=57)
items_listbox.pack()

horizontal_button = tk.Frame(root)
horizontal_button.pack()


btn_read = tk.Button(horizontal_button, text= 'Ler', command=read, width=15)
btn_read.pack(side= tk.LEFT)

btn_update = tk.Button(horizontal_button, text ='Atualizar', command=update, width=15)
btn_update.pack(side= tk.LEFT)

btn_delete = tk.Button(horizontal_button, text= 'Deletar', command=delete, width=15)
btn_delete.pack(side= tk.LEFT)



root.mainloop()