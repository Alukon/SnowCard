from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()
root.title('С Новеньким Годом!')
root.resizable(width=True, height=True)
cWidht = 1100
cHeidht = 632
c = Canvas(root, width=cWidht, height=cHeidht, bg='#002655')

c.pack()

image = ImageTk.PhotoImage(file='elka.png')
c.create_image(100, 100, image=image, anchor=NW)


def createText():
    cText = ('''
Пусть 2023-й будет годом счастья,
Годом искренних улыбок, нежности,
Увлекательных открытий, впечатлений,
Годом смеха, позитива и объятий жарких.

Пусть 2023-й будет годом мира,
Благоденствия, достатка, праздника,
Закружит пусть бесконечным хороводом,
Поздравляю вас с Новым годом!

    ''')
    c.create_text(cWidht * 2 / 3, cHeidht / 2, text=cText, fill='white', font='Times 24 bold')


def createSnow(t, n):
    for i in range(500):
        x = random.randint(1, cWidht)
        y = random.randint(-cHeidht * n - 8, cHeidht * (1 - n))
        w = random.randint(3, 8)
        c.create_oval(x, y, x + w, y + w, fill='white', tag=t)


def motion():
    global indicator, indicator_count
    c.move('tagOne', 0, 1)
    c.move('tagTwo', 0, 1)
    c.move(indicator, 0, 1)
# если снежинки выходят за пределы
    if c.coords(indicator)[1] < cHeidht +1:
        root.after(20, motion)
    else:
        c.move(indicator, 0, -cHeidht - 5)
        root.after(20, motion)
        if indicator_count == 0:
            c.delete('tgOne')
            createSnow('tagOne', 1)
            indicator_count = 1
        else:
            c.delete('tgTwo')
            createSnow('tagTwo', 1)
            indicator_count = 0

def main():
    global indicator, indicator_count

    indicator = c.create_oval(23, 5, 28, 8, fill='white')
    indicator_count = 0

    createText()
    createSnow('tagOne', 0)
    createSnow('tagOne', 1)

    motion()


main()

root.mainloop()
