# import tkinter
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

var = tk.StringVar()
# label_1 = tk.Label(window, text='Hello world!', bg='green', font=('Arial',12), width=15, height=2)
label_1 = tk.Label(window, textvariable=var, bg='green', font=('Arial',12), width=15, height=2)
label_1.pack()

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('You hit me!')
    else:
        on_hit = False
        var.set('')
btn_1 = tk.Button(window, text='hit me', width=15, height=2, command=hit_me)
btn_1.pack()

window.mainloop()
