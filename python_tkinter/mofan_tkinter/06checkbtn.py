# import tkinter
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

label_1 = tk.Label(window, bg='yellow', width=20, text='empty')
label_1.pack()

def print_selection():
    print_str = ''
    if(var1.get() == 1) & (var2.get() == 0):
        print_str = 'I love only Python'
    elif (var1.get() == 0) & (var2.get() == 1):
        print_str = 'I love only C++'
    elif (var1.get() == 0) & (var2.get() == 0):
        print_str = 'I do not love either'
    else:
        print_str = 'I love both'
    label_1.config(text=print_str)

var1 = tk.IntVar()
var2 = tk.IntVar()
checkbtn_1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0,
                            command=print_selection)
checkbtn_1.pack()
checkbtn_2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0,
                            command=print_selection)
checkbtn_2.pack()

window.mainloop()
