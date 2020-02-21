import random
from tkinter import messagebox

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1


def box_click_control():
    global b0, b1, b2, b3, b10, b11, b12, b13, b20, b21, b22, b23, b30, b31, b32, b33
    b0 = 0
    b1 = 0
    b2 = 0
    b3 = 0
    b10 = 0
    b11 = 0
    b12 = 0
    b13 = 0
    b20 = 0
    b21 = 0
    b22 = 0
    b23 = 0
    b30 = 0
    b31 = 0
    b32 = 0
    b33 = 0


def list_create():
    global list
    list = [*range(1,17)]


def get_random():
    global a, first_four, next_four, next2_four, last_four, busted
    first_four = False
    next_four = False
    next2_four = False
    last_four = False
    busted = False
    a = random.choice(list)
    if a > 0 and a < 5:
        first_four = True
    if a > 4 and a < 9:
        next_four = True
    if a > 8 and a < 13:
        next2_four = True
    if a > 12 and a < 17:
        last_four = True
    if a == 0:
        busted = True
    list.remove(a)
    print(a)
    print(list)
    """""
    if a == 3:
        w.left0.configure(image=w._success_left1)
        w.left0.place(x=56, y=56)
    if a == 4:
        w.right0.configure(image=w._success_right1)
        w.right0.place(x=954, y=56)
    if a == 7:
        w.left1.configure(image=w._success_left2)
        w.left1.place(x=56, y=218)
    if a == 8:
        w.right1.configure(image=w._success_right2)
        w.right1.place(x=954, y=218)
    if a == 11:
        w.left2.configure(image=w._success_left3)
        w.left2.place(x=56, y=380)
    if a == 12:
        w.right2.configure(image=w._success_right3)
        w.right2.place(x=954, y=380)
    if a == 14:
        w.left3.configure(image=w._success_left4)
        w.left3.place(x=56, y=542)
    if a == 15:
        w.right3.configure(image=w._success_right4)
        w.right3.place(x=954, y=542)"""""


def game_end_cont():
    global b0, b1, b2, b3, b10, b11, b12, b13, b20, b21, b22, b23, b30, b31, b32, b33
    if list == []:
        w.lvl1.configure(state="normal")
        messagebox.showinfo(title="TUTORIAL COMPLETED", message="Go back menu and choose LAMER 1 on Level TAB.")


def game_busted_cont():
    empty_function = 1


def box0_cont(event):
    global b0
    if b0 == 0:
        get_random()
        w.box0.destroy()
        w.opened_box0.place(x=306, y=56, height=160, width=160)
        if first_four is True:
            b0 = 1
            w.opened_box0.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b0 = 2
            w.opened_box0.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b0 = 3
            w.opened_box0.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b0 = 4
            w.opened_box0.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b0 = 5
            w.opened_box0.configure(image=w._busted)
            game_busted_cont()


def busted_box0_cont():
    global b0
    if b0 == 0:
        get_random()
        w.box0.destroy()
        w.opened_box0.place(x=306, y=56, height=160, width=160)
        if first_four is True:
            b0 = 1
            w.opened_box0.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b0 = 2
            w.opened_box0.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b0 = 3
            w.opened_box0.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b0 = 4
            w.opened_box0.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b0 = 5
            game_busted_cont()


def box1_cont(event):
    global b1
    if b1 == 0:
        get_random()
        w.box1.destroy()
        w.opened_box1.place(x=468, y=56, height=160, width=160)
        if first_four is True:
            b1 = 1
            w.opened_box1.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b1 = 2
            w.opened_box1.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b1 = 3
            w.opened_box1.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b1 = 4
            w.opened_box1.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b1 = 5
            w.opened_box1.configure(image=w._busted)
            game_busted_cont()


def busted_box1_cont():
    global b1
    if b1 == 0:
        get_random()
        w.box1.destroy()
        w.opened_box1.place(x=468, y=56, height=160, width=160)
        if first_four is True:
            b1 = 1
            w.opened_box1.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b1 = 2
            w.opened_box1.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b1 = 3
            w.opened_box1.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b1 = 4
            w.opened_box1.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b1 = 5
            w.opened_box1.configure(image=w._busted)
            game_busted_cont()


def box2_cont(event):
    global b2
    if b2 == 0:
        get_random()
        w.box2.destroy()
        w.opened_box2.place(x=630, y=56, height=160, width=160)
        if first_four is True:
            b2 = 1
            w.opened_box2.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b2 = 2
            w.opened_box2.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b2 = 3
            w.opened_box2.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b2 = 4
            w.opened_box2.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b2 = 5
            w.opened_box2.configure(image=w._busted)
            game_busted_cont()


def busted_box2_cont():
    global b2
    if b2 == 0:
        get_random()
        w.box2.destroy()
        w.opened_box2.place(x=630, y=56, height=160, width=160)
        if first_four is True:
            b2 = 1
            w.opened_box2.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b2 = 2
            w.opened_box2.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b2 = 3
            w.opened_box2.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b2 = 4
            w.opened_box2.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b2 = 5
            w.opened_box2.configure(image=w._busted)
            game_busted_cont()


def box3_cont(event):
    global b3
    if b3 == 0:
        get_random()
        w.box3.destroy()
        w.opened_box3.place(x=792, y=56, height=160, width=160)
        if first_four is True:
            b3 = 1
            w.opened_box3.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b3 = 2
            w.opened_box3.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b3 = 3
            w.opened_box3.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b3 = 4
            w.opened_box3.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b3 = 5
            w.opened_box3.configure(image=w._busted)
            game_busted_cont()


def busted_box3_cont():
    global b3
    if b3 == 0:
        get_random()
        w.box3.destroy()
        w.opened_box3.place(x=792, y=56, height=160, width=160)
        if first_four is True:
            b3 = 1
            w.opened_box3.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b3 = 2
            w.opened_box3.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b3 = 3
            w.opened_box3.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b3 = 4
            w.opened_box3.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b3 = 5
            w.opened_box3.configure(image=w._busted)
            game_busted_cont()


def box10_cont(event):
    global b10
    if b10 == 0:
        get_random()
        w.box10.destroy()
        w.opened_box10.place(x=306, y=218, height=160, width=160)
        if first_four is True:
            b10 = 1
            w.opened_box10.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b10 = 2
            w.opened_box10.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b10 = 3
            w.opened_box10.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b10 = 4
            w.opened_box10.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b10 = 5
            w.opened_box10.configure(image=w._busted)
            game_busted_cont()


def busted_box10_cont():
    global b10
    if b10 == 0:
        get_random()
        w.box10.destroy()
        w.opened_box10.place(x=306, y=218, height=160, width=160)
        if first_four is True:
            b10 = 1
            w.opened_box10.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b10 = 2
            w.opened_box10.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b10 = 3
            w.opened_box10.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b10 = 4
            w.opened_box10.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b10 = 5
            w.opened_box10.configure(image=w._busted)
            game_busted_cont()


def box11_cont(event):
    global b11
    if b11 == 0:
        get_random()
        w.box11.destroy()
        w.opened_box11.place(x=468, y=218, height=160, width=160)
        if first_four is True:
            b11 = 1
            w.opened_box11.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b11 = 2
            w.opened_box11.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b11 = 3
            w.opened_box11.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b11 = 4
            w.opened_box11.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b11 = 5
            w.opened_box11.configure(image=w._busted)
            game_busted_cont()


def busted_box11_cont():
    global b11
    if b11 == 0:
        get_random()
        w.box11.destroy()
        w.opened_box11.place(x=468, y=218, height=160, width=160)
        if first_four is True:
            b11 = 1
            w.opened_box11.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b11 = 2
            w.opened_box11.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b11 = 3
            w.opened_box11.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b11 = 4
            w.opened_box11.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b11 = 5
            w.opened_box11.configure(image=w._busted)
            game_busted_cont()


def box12_cont(event):
    global b12
    if b12 == 0:
        get_random()
        w.box12.destroy()
        w.opened_box12.place(x=630, y=218, height=160, width=160)
        if first_four is True:
            b12 = 1
            w.opened_box12.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b12 = 2
            w.opened_box12.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b12 = 3
            w.opened_box12.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b12 = 4
            w.opened_box12.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b12 = 5
            w.opened_box12.configure(image=w._busted)
            game_busted_cont()


def busted_box12_cont():
    global b12
    if b12 == 0:
        get_random()
        w.box12.destroy()
        w.opened_box12.place(x=630, y=218, height=160, width=160)
        if first_four is True:
            b12 = 1
            w.opened_box12.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b12 = 2
            w.opened_box12.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b12 = 3
            w.opened_box12.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b12 = 4
            w.opened_box12.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b12 = 5
            w.opened_box12.configure(image=w._busted)
            game_busted_cont()


def box13_cont(event):
    global b13
    if b13 == 0:
        get_random()
        w.box13.destroy()
        w.opened_box13.place(x=792, y=218, height=160, width=160)
        if first_four is True:
            b13 = 1
            w.opened_box13.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b13 = 2
            w.opened_box13.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b13 = 3
            w.opened_box13.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b13 = 4
            w.opened_box13.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b13 = 5
            w.opened_box13.configure(image=w._busted)
            game_busted_cont()


def busted_box13_cont():
    global b13
    if b13 == 0:
        get_random()
        w.box13.destroy()
        w.opened_box13.place(x=792, y=218, height=160, width=160)
        if first_four is True:
            b13 = 1
            w.opened_box13.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b13 = 2
            w.opened_box13.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b13 = 3
            w.opened_box13.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b13 = 4
            w.opened_box13.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b13 = 5
            w.opened_box13.configure(image=w._busted)
            game_busted_cont()


def box20_cont(event):
    global b20
    if b20 == 0:
        get_random()
        w.box20.destroy()
        w.opened_box20.place(x=306, y=380, height=160, width=160)
        if first_four is True:
            b20 = 1
            w.opened_box20.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b20 = 2
            w.opened_box20.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b20 = 3
            w.opened_box20.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b20 = 4
            w.opened_box20.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b20 = 5
            w.opened_box20.configure(image=w._busted)
            game_busted_cont()


def busted_box20_cont():
    global b20
    if b20 == 0:
        get_random()
        w.box20.destroy()
        w.opened_box20.place(x=306, y=380, height=160, width=160)
        if first_four is True:
            b20 = 1
            w.opened_box20.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b20 = 2
            w.opened_box20.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b20 = 3
            w.opened_box20.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b20 = 4
            w.opened_box20.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b20 = 5
            w.opened_box20.configure(image=w._busted)
            game_busted_cont()


def box21_cont(event):
    global b21
    if b21 == 0:
        get_random()
        w.box21.destroy()
        w.opened_box21.place(x=468, y=380, height=160, width=160)
        if first_four is True:
            b21 = 1
            w.opened_box21.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b21 = 2
            w.opened_box21.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b21 = 3
            w.opened_box21.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b21 = 4
            w.opened_box21.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b21 = 5
            w.opened_box21.configure(image=w._busted)
            game_busted_cont()


def busted_box21_cont():
    global b21
    if b21 == 0:
        get_random()
        w.box21.destroy()
        w.opened_box21.place(x=468, y=380, height=160, width=160)
        if first_four is True:
            b21 = 1
            w.opened_box21.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b21 = 2
            w.opened_box21.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b21 = 3
            w.opened_box21.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b21 = 4
            w.opened_box21.configure(image=w._success3)
            game_end_cont()
        if busted is True:
            b21 = 5
            w.opened_box21.configure(image=w._busted)
            game_busted_cont()


def box22_cont(event):
    global b22
    if b22 == 0:
        get_random()
        w.box22.destroy()
        w.opened_box22.place(x=630, y=380, height=160, width=160)
        if first_four is True:
            b22 = 1
            w.opened_box22.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b22 = 2
            w.opened_box22.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b22 = 3
            w.opened_box22.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b22 = 4
            w.opened_box22.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b22 = 5
            w.opened_box22.configure(image=w._busted)
            game_busted_cont()


def busted_box22_cont():
    global b22
    if b22 == 0:
        get_random()
        w.box22.destroy()
        w.opened_box22.place(x=630, y=380, height=160, width=160)
        if first_four is True:
            b22 = 1
            w.opened_box22.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b22 = 2
            w.opened_box22.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b22 = 3
            w.opened_box22.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b22 = 4
            w.opened_box22.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b22 = 5
            w.opened_box22.configure(image=w._busted)
            game_busted_cont()


def box23_cont(event):
    global b23
    if b23 == 0:
        get_random()
        w.box23.destroy()
        w.opened_box23.place(x=792, y=380, height=160, width=160)
        if first_four is True:
            b23 = 1
            w.opened_box23.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b23 = 2
            w.opened_box23.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b23 = 3
            w.opened_box23.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b23 = 4
            w.opened_box23.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b23 = 5
            w.opened_box23.configure(image=w._busted)
            game_busted_cont()


def busted_box23_cont():
    global b23
    if b23 == 0:
        get_random()
        w.box23.destroy()
        w.opened_box23.place(x=792, y=380, height=160, width=160)
        if first_four is True:
            b23 = 1
            w.opened_box23.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b23 = 2
            w.opened_box23.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b23 = 3
            w.opened_box23.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b23 = 4
            w.opened_box23.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b23 = 5
            w.opened_box23.configure(image=w._busted)
            game_busted_cont()


def box30_cont(event):
    global b30
    if b30 == 0:
        get_random()
        w.box30.destroy()
        w.opened_box30.place(x=306, y=542, height=160, width=160)
        if first_four is True:
            b30 = 1
            w.opened_box30.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b30 = 2
            w.opened_box30.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b30 = 3
            w.opened_box30.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b30 = 4
            w.opened_box30.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b30 = 5
            w.opened_box30.configure(image=w._busted)
            game_busted_cont()


def busted_box30_cont():
    global b30
    if b30 == 0:
        get_random()
        w.box30.destroy()
        w.opened_box30.place(x=306, y=542, height=160, width=160)
        if first_four is True:
            b30 = 1
            w.opened_box30.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b30 = 2
            w.opened_box30.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b30 = 3
            w.opened_box30.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b30 = 4
            w.opened_box30.configure(image=w._success3)
            game_end_cont()
        if busted is True:
            b30 = 5
            w.opened_box30.configure(image=w._busted)
            game_busted_cont()


def box31_cont(event):
    global b31
    if b31 == 0:
        get_random()
        w.box31.destroy()
        w.opened_box31.place(x=468, y=542, height=160, width=160)
        if first_four is True:
            b31 = 1
            w.opened_box31.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b31 = 2
            w.opened_box31.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b31 = 3
            w.opened_box31.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b31 = 4
            w.opened_box31.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b31 = 5
            w.opened_box31.configure(image=w._busted)
            game_busted_cont()


def busted_box31_cont():
    global b31
    if b31 == 0:
        get_random()
        w.box31.destroy()
        w.opened_box31.place(x=468, y=542, height=160, width=160)
        if first_four is True:
            b31 = 1
            w.opened_box31.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b31 = 2
            w.opened_box31.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b31 = 3
            w.opened_box31.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b31 = 4
            w.opened_box31.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b31 = 5
            w.opened_box31.configure(image=w._busted)
            game_busted_cont()


def box32_cont(event):
    global b32
    if b32 == 0:
        get_random()
        w.box32.destroy()
        w.opened_box32.place(x=630, y=542, height=160, width=160)
        if first_four is True:
            b32 = 1
            w.opened_box32.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b32 = 2
            w.opened_box32.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b32 = 3
            w.opened_box32.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b32 = 4
            w.opened_box32.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b32 = 5
            w.opened_box32.configure(image=w._busted)
            game_busted_cont()


def busted_box32_cont():
    global b32
    if b32 == 0:
        get_random()
        w.box32.destroy()
        w.opened_box32.place(x=630, y=542, height=160, width=160)
        if first_four is True:
            b32 = 1
            w.opened_box32.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b32 = 2
            w.opened_box32.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b32 = 3
            w.opened_box32.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b32 = 4
            w.opened_box32.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b32 = 5
            w.opened_box32.configure(image=w._busted)
            game_busted_cont()


def box33_cont(event):
    global b33
    if b33 == 0:
        get_random()
        w.box33.destroy()
        w.opened_box33.place(x=792, y=542, height=160, width=160)
        if first_four is True:
            b33 = 1
            w.opened_box33.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b33 = 2
            w.opened_box33.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b33 = 3
            w.opened_box33.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b33 = 4
            w.opened_box33.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b33 = 5
            w.opened_box33.configure(image=w._busted)
            game_busted_cont()


def busted_box33_cont():
    global b33
    if b33 == 0:
        get_random()
        w.box33.destroy()
        w.opened_box33.place(x=792, y=542, height=160, width=160)
        if first_four is True:
            b33 = 1
            w.opened_box33.configure(image=w._success0)
            game_end_cont()
        elif next_four is True:
            b33 = 2
            w.opened_box33.configure(image=w._success1)
            game_end_cont()
        elif next2_four is True:
            b33 = 3
            w.opened_box33.configure(image=w._success2)
            game_end_cont()
        elif last_four is True:
            b33 = 4
            w.opened_box33.configure(image=w._success3)
            game_end_cont()
        elif busted is True:
            b33 = 5
            w.opened_box33.configure(image=w._busted)
            game_busted_cont()


def init(app, gui, *args, **kwargs):
    global w, root
    w = gui
    root = app

