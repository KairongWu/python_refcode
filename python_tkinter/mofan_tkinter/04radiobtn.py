# import tkinter
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

var = tk.StringVar()
label_1 = tk.Label(window, text='empty', bg='yellow', width=20)
label_1.pack()

def print_selection():
    label_1.config(text='you have selected ' + var.get())

radiobtn_1 = tk.Radiobutton(window, text='Option A', variable=var, value='A', command=print_selection)
radiobtn_1.pack()

radiobtn_2 = tk.Radiobutton(window, text='Option B', variable=var, value='B', command=print_selection)
radiobtn_2.pack()

radiobtn_3 = tk.Radiobutton(window, text='Option C', variable=var, value='C', command=print_selection)
radiobtn_3.pack()

window.mainloop()