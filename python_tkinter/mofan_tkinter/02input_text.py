# import tkinter
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

entry_1 = tk.Entry(window, show=None)
# entry_1 = tk.Entry(window, show='*')
entry_1.pack()
def insert_point():
    var = entry_1.get()
    text_1.insert('insert', var)

def insert_end():
    var = entry_1.get()
    text_1.insert('end', var)
    # text_1.insert(1.1, var)

btn_1 = tk.Button(window, text='insert point', width=15, height=2, command=insert_point)
btn_1.pack()
btn_2 = tk.Button(window, text='insert end', width=15, height=2, command=insert_end)
btn_2.pack()

text_1 = tk.Text(window, height=2)
text_1.pack()


window.mainloop()