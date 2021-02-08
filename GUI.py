import tkinter as tk

HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='blue')
frame.place(relx=0.1, rely=0.1, relheight=0.7, relwidth=0.7)

button = tk.Button(root, text='start', bg='gray', fg='red')
button.pack()


root.mainloop()