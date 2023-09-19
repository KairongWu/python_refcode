# import tkinter
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

def hit_me():
    # messagebox.showinfo(title='Hi', message='hahahahah')
    # messagebox.showwarning(title='Hi', message='nonononono')
    # messagebox.showerror(title='Hi', message='No! never')
    # print(messagebox.askquestion(title='Hi', message='hahahahah'))  # return 'yes' or 'no'
    # print(messagebox.askyesno(title='Hi', message='hahahahah'))  # return 'True' or 'False'
    # print(messagebox.askokcancel(title='Hi', message='hahahahah'))  # return 'True' or 'False'
    print(messagebox.askretrycancel(title='Hi', message='hahahahah'))  # return 'True' or 'False'

btn_1 = tk.Button(window, text='Hit me', command=hit_me).pack()

window.mainloop()
