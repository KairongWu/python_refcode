# import tkinter
import tkinter as tk


window = tk.Tk()
window.title('my window')
window.geometry('200x300')

var1 = tk.StringVar()


label_1 = tk.Label(window, textvariable=var1, bg='yellow', font=('Arian',12), width=4)
label_1.pack()

def print_selection():
    value = listbox_1.get(listbox_1.curselection())
    var1.set(value)

btn_1 = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
btn_1.pack()

var2 = tk.StringVar()
var2.set((11, 22, 33, 44, 55))
listbox_1 = tk.Listbox(window, listvariable=var2)
list_items = [1,2,3,4]
for item in list_items:
    listbox_1.insert('end', item)
listbox_1.insert(1, 'first')
listbox_1.insert(2, 'second')
listbox_1.delete(2)
listbox_1.pack()

window.mainloop()