from tkinter import *


window = Tk()
window.title("Cica") 
canvas = Canvas(window, width=500, height=500)
canvas.pack()

my_image = PhotoImage(file="c:\\Users\\backandras\\Desktop\\Munka\\Marcsi vicces.png")
canvas.create_image(0, 0, anchor = NW, image=my_image)

window.mainloop()