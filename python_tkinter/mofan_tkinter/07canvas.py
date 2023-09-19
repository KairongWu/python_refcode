# import tkinter
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

canvas_1 = tk.Canvas(window, bg='blue', height=100, width=200)
canvas_1.pack()

image_file = tk.PhotoImage(file='./luffy.png')
image = canvas_1.create_image(0, 0, anchor='nw', image=image_file)

x0, y0, x1, y1 = 50, 50, 80, 80
line = canvas_1.create_line(x0, y0, x1, y1)
oval = canvas_1.create_oval(x0, y0, x1, y1, fill='red')
arc = canvas_1.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)
rect = canvas_1.create_rectangle(100, 30, 100+20, 30+20)

def moveit():
    canvas_1.move(rect, 0, 2)

btn_1 = tk.Button(window, text='move', command=moveit).pack()

window.mainloop()