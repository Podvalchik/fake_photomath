from tkinter import *
from math import *


def getCoords(smin, smax, lim):
    s = abs(smax) + abs(smin) + 1
    sN = min(s, lim)
    dx = round(s / sN, 1)

    coords = []
    i = 0
    while i + dx <= smax:
        i += dx
        coords.append(round(i, 1))

    coords.insert(0, 0)

    i = 0
    while i - dx >= smin:
        i -= dx
        coords.insert(0, round(i, 1))

    return coords


def osi():
    global xmin, xmax, ymin, ymax, width, height

    xmax = int(ent_xmax.get())
    xmin = int(ent_xmin.get())
    ymax = int(ent_ymax.get())
    ymin = int(ent_ymin.get())
    width = int(ent_width.get())
    height = int(ent_height.get())

    marginX, marginY = 25, 25  # отступы
    c.create_rectangle(0, 0, width, height, fill='#FFFFFF')  # поле под график

    rDx = getCoords(xmin, xmax, 21)  # подписи рисок по х
    rDy = getCoords(ymin, ymax, 21)  # подписи рисок по y
    rNumX = len(rDx)  # всего рисок по х
    rNumY = len(rDy)  # всего рисок по y
    dx = (width - (marginX * 2)) / (rNumX - 1)  # ширина риски по х
    dy = (height - (marginY * 2)) / (rNumY - 1)  # ширина риски по y

    print(rDx, rDy)
    for i in range(0, rNumX, 1):
        rx = dx * i + marginX
        c.create_line(rx, 0, rx, height, width=1, fill="#AAAAAA")  # сетка по y
        if rDx[i] == 0:
            c.create_line(rx, 0, rx, height, width=2)  # ось y
            c.create_polygon(rx - 10, 10, rx, 0, rx + 10, 10)  # треугольник по оси y
            c.create_text(rx + 18, 10, text="Y")  # подпись оси у
            for j in range(0, rNumY, 1):
                if rDy[j] == 0:
                    continue
                ry = dy * j + marginY
                c.create_line(rx, ry, rx + 5, ry, width=1)  # риска у
                c.create_text(rx + 15, ry + 6, text=rDy[j])  # подпись риски у

    for i in range(0, rNumY, 1):
        ry = dy * i + marginY
        c.create_line(0, ry, width, ry, width=1, fill="#AAAAAA")  # сетка по x
        if rDy[i] == 0:
            c.create_line(0, ry, width - 5, ry, width=2)  # ось x
            c.create_polygon(width - 10, ry - 10, width, ry, width - 10, ry + 10)  # треугольник по оси x
            c.create_text(height - 8, ry + 20, text="X")  # подпись оси х
            for j in range(0, rNumX, 1):
                rx = dx * j + marginX
                if rDx[j] == 0:
                    c.create_text(rx + 15, ry + 15, text=rDx[j])  # риска 0
                    continue
                c.create_line(rx, ry, rx, ry + 5, width=1)  # риска х
                c.create_text(rx, ry + 15, text=rDx[j])  # подпись риски х


def nx(x):
    global xmin, xmax, width
    return round((x - xmin) / (xmax - xmin) * width)


def ny(y):
    global ymax, ymin, height
    return round((y - ymax) / (ymax - ymin) * height)


def makegraf():
    global xmax, xmin, ymax, ymin, in_graf, width, height
    in_graf = ent_fn.get()
    x = xmin
    while x <= xmax:
        px, py = nx(x), -ny(eval(in_graf))
        if px > 0 and px < width and py > 0 and py < height:
            c.create_line(px, py, px + 1, py + 1, fill='#FF0000', width=2)
        x = x + dx


def prep():
    c.delete('all')
    osi()


def graf_clear():
    c.delete('all')
    osi()


root = Tk()

screenWidth = root.winfo_screenwidth() - 100  # ширина экрана из системы
screenHeight = root.winfo_screenheight() - 100  # высота экрана из системы
xmin, xmax = -10, 10  # х (min х max)
ymin, ymax = -10, 10  # y (min х max)
width, height = screenHeight * 3 // 4, screenHeight * 3 // 4  # высота х ширина
in_graf = "1/(x*(x+2))"  # функция
dx = 0.001  # точность
bgColor = '#3399CC'  # цвет панели
сanvasColor = '#99CCFF'  # цвет канвы

root.geometry(str(screenWidth) + "x" + str(screenHeight) + "+0+0")

pn_control = Frame(root, height=67, bg=bgColor)
pn_control.pack(side='top', fill='x')

pn_graph = Frame(root)
pn_graph.pack(side="bottom", fill="both", expand=1)

c = Canvas(pn_graph, bg=сanvasColor)
c.pack(fill="both", expand=1)

y_top = 10
h_top = 18

lb_width = Label(pn_control, text='График (Ш х В):', background=bgColor, justify=CENTER)
lb_width.place(x=10, y=y_top, width=95, height=h_top)
ent_width = Entry(pn_control, justify=CENTER)
ent_width.place(x=105, y=y_top, width=50, height=h_top)
ent_width.insert(END, width)

lb_x = Label(pn_control, text=' x ', background=bgColor)
lb_x.place(x=160, y=y_top, width=10, height=h_top)

ent_height = Entry(pn_control, justify=CENTER)
ent_height.place(x=175, y=y_top, width=50, height=h_top)
ent_height.insert(END, height)

lb_xmin = Label(pn_control, text='x (min : max):', background=bgColor)
lb_xmin.place(x=235, y=y_top, width=100, height=h_top)

ent_xmin = Entry(pn_control, justify=CENTER)
ent_xmin.place(x=330, y=y_top, width=50, height=h_top)
ent_xmin.insert(END, xmin)

lb_xmax = Label(pn_control, text=' : ', background=bgColor)
lb_xmax.place(x=385, y=y_top, width=10, height=h_top)

ent_xmax = Entry(pn_control, justify=CENTER)
ent_xmax.place(x=400, y=y_top, width=50, height=h_top)
ent_xmax.insert(END, xmax)

lb_ymin = Label(pn_control, text='y (min : max):', background=bgColor)
lb_ymin.place(x=455, y=y_top, width=100, height=h_top)

ent_ymin = Entry(pn_control, justify=CENTER)
ent_ymin.place(x=555, y=y_top, width=50, height=h_top)
ent_ymin.insert(END, ymin)

lb_ymax = Label(pn_control, text=' : ', background=bgColor)
lb_ymax.place(x=610, y=y_top, width=10, height=h_top)

ent_ymax = Entry(pn_control, justify=CENTER)
ent_ymax.place(x=625, y=y_top, width=50, height=h_top)
ent_ymax.insert(END, ymax)

lb_fn = Label(pn_control, text=' f(y) ', background=bgColor)
lb_fn.place(x=685, y=y_top, width=40, height=h_top)

ent_fn = Entry(pn_control, justify=CENTER)
ent_fn.place(x=725, y=y_top, width=120, height=h_top)
ent_fn.insert(END, in_graf)

y_bt = 40;
h_bt = 20;
w_bt = 87
bt_prep = Button(pn_control, text="Подготовить", foreground='#20B2AA', command=prep)
bt_prep.place(x=20, y=y_bt, width=w_bt, height=h_bt)

bt_draw = Button(pn_control, text="Начертить", foreground='#00BFFF', command=makegraf)
bt_draw.place(x=170, y=y_bt, width=w_bt, height=h_bt)

bt_clear = Button(pn_control, text="Очистить", foreground='#6495ED', command=graf_clear)
bt_clear.place(x=363, y=y_bt, width=w_bt, height=h_bt)

root.mainloop()
