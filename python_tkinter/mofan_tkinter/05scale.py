# import tkinter
import tkinter as tk


window = tk.Tk()
window.title("my window")
window.geometry('200x200')

label_1 = tk.Label(window, bg='yellow', width=20, text='empty')
label_1.pack()

def print_selection(v):
    label_1.config(text='you have selected ' + v)

scale_1 = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL,
                   length=200, showvalue=True, tickinterval=3, resolution=0.01,
                   command=print_selection)
scale_1.pack()

window.mainloop()