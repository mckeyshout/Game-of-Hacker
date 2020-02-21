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
    list = [*range(1, 17)]


def get_random():
    global a, first_four, next_four, next2_four, last_four, busted
    first_four = False
    next_four = False
    next2_four = False
    last_four = False
    busted = False
    a = random.choice(list)
    if a == 16:
        last_four = True
    else:
        busted = True
    list.remove(a)
    print(a)
    print(list)


def game_end_cont():
    global b0, b1, b2, b3, b10, b11, b12, b13, b20, b21, b22, b23, b30, b31, b32, b33
    if list == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
        w.lvl15.configure(state="normal")

        def b0_cc():
            if b0 == 0:
                w.box0.destroy()
                w.opened_box0.configure(image=w._hacked15)
                w.opened_box0.place(x=306, y=56, height=160, width=160)

        def b1_cc():
            if b1 == 0:
                w.box1.destroy()
                w.opened_box1.configure(image=w._hacked15)
                w.opened_box1.place(x=468, y=56, height=160, width=160)

        def b2_cc():
            if b2 == 0:
                w.box2.destroy()
                w.opened_box2.configure(image=w._hacked15)
                w.opened_box2.place(x=630, y=56, height=160, width=160)

        def b3_cc():
            if b3 == 0:
                w.box3.destroy()
                w.opened_box3.configure(image=w._hacked15)
                w.opened_box3.place(x=792, y=56, height=160, width=160)

        def b10_cc():
            if b10 == 0:
                w.box10.destroy()
                w.opened_box10.configure(image=w._hacked15)
                w.opened_box10.place(x=306, y=218, height=160, width=160)

        def b11_cc():
            if b11 == 0:
                w.box11.destroy()
                w.opened_box11.configure(image=w._hacked15)
                w.opened_box11.place(x=468, y=218, height=160, width=160)

        def b12_cc():
            if b12 == 0:
                w.box12.destroy()
                w.opened_box12.configure(image=w._hacked15)

                w.opened_box12.place(x=630, y=218, height=160, width=160)
        def b13_cc():
            if b13 == 0:
                w.box13.destroy()
                w.opened_box13.configure(image=w._hacked15)
                w.opened_box13.place(x=792, y=218, height=160, width=160)

        def b20_cc():
            if b20 == 0:
                w.box20.destroy()
                w.opened_box20.configure(image=w._hacked15)
                w.opened_box20.place(x=306, y=380, height=160, width=160)

        def b21_cc():
            if b21 == 0:
                w.box21.destroy()
                w.opened_box21.configure(image=w._hacked15)
                w.opened_box21.place(x=468, y=380, height=160, width=160)

        def b22_cc():
            if b22 == 0:
                w.box22.destroy()
                w.opened_box22.configure(image=w._hacked15)
                w.opened_box22.place(x=630, y=380, height=160, width=160)

        def b23_cc():
            if b23 == 0:
                w.box23.destroy()
                w.opened_box23.configure(image=w._hacked15)
                w.opened_box23.place(x=792, y=380, height=160, width=160)

        def b30_cc():
            if b30 == 0:
                w.box30.destroy()
                w.opened_box30.configure(image=w._hacked15)
                w.opened_box30.place(x=306, y=542, height=160, width=160)

        def b31_cc():
            if b31 == 0:
                w.box31.destroy()
                w.opened_box31.configure(image=w._hacked15)
                w.opened_box31.place(x=468, y=542, height=160, width=160)

        def b32_cc():
            if b32 == 0:
                w.box32.destroy()
                w.opened_box32.configure(image=w._hacked15)
                w.opened_box32.place(x=630, y=542, height=160, width=160)

        def b33_cc():
            if b33 == 0:
                w.box33.destroy()
                w.opened_box33.configure(image=w._hacked15)
                w.opened_box33.place(x=792, y=542, height=160, width=160)

        b0_cc()
        b1_cc()
        b2_cc()
        b3_cc()
        b10_cc()
        b11_cc()
        b12_cc()
        b13_cc()
        b20_cc()
        b21_cc()
        b22_cc()
        b23_cc()
        b30_cc()
        b31_cc()
        b32_cc()
        b33_cc()
        messagebox.showinfo(title="CONGRATULATIONS", message="YOU ARE MASTER ON HACK. YOU HACKED THE WHOLE WORLD!")


def game_busted_cont():
    def b0_c():
        if b0 == 1:
            w.opened_box0.configure(image=w._success0)
        if b0 == 2:
            w.opened_box0.configure(image=w._success1)
        if b0 == 3:
            w.opened_box0.configure(image=w._success2)
        if b0 == 4:
            w.opened_box0.configure(image=w._success3)
        if b0 == 5:
            w.opened_box0.configure(image=w._busted)

    def b1_c():
        if b1 == 1:
            w.opened_box1.configure(image=w._success0)
        if b1 == 2:
            w.opened_box1.configure(image=w._success1)
        if b1 == 3:
            w.opened_box1.configure(image=w._success2)
        if b1 == 4:
            w.opened_box1.configure(image=w._success3)
        if b1 == 5:
            w.opened_box1.configure(image=w._busted)

    def b2_c():
        if b2 == 1:
            w.opened_box2.configure(image=w._success0)
        if b2 == 2:
            w.opened_box2.configure(image=w._success1)
        if b2 == 3:
            w.opened_box2.configure(image=w._success2)
        if b2 == 4:
            w.opened_box2.configure(image=w._success3)
        if b2 == 5:
            w.opened_box2.configure(image=w._busted)

    def b3_c():
        if b3 == 1:
            w.opened_box3.configure(image=w._success0)
        if b3 == 2:
            w.opened_box3.configure(image=w._success1)
        if b3 == 3:
            w.opened_box3.configure(image=w._success2)
        if b3 == 4:
            w.opened_box3.configure(image=w._success3)
        if b3 == 5:
            w.opened_box3.configure(image=w._busted)

    def b10_c():
        if b10 == 1:
            w.opened_box10.configure(image=w._success0)
        if b10 == 2:
            w.opened_box10.configure(image=w._success1)
        if b10 == 3:
            w.opened_box10.configure(image=w._success2)
        if b10 == 4:
            w.opened_box10.configure(image=w._success3)
        if b10 == 5:
            w.opened_box10.configure(image=w._busted)

    def b11_c():
        if b11 == 1:
            w.opened_box11.configure(image=w._success0)
        if b11 == 2:
            w.opened_box11.configure(image=w._success1)
        if b11 == 3:
            w.opened_box11.configure(image=w._success2)
        if b11 == 4:
            w.opened_box11.configure(image=w._success3)
        if b11 == 5:
            w.opened_box11.configure(image=w._busted)

    def b12_c():
        if b12 == 1:
            w.opened_box12.configure(image=w._success0)
        if b12 == 2:
            w.opened_box12.configure(image=w._success1)
        if b12 == 3:
            w.opened_box12.configure(image=w._success2)
        if b12 == 4:
            w.opened_box12.configure(image=w._success3)
        if b12 == 5:
            w.opened_box12.configure(image=w._busted)

    def b13_c():
        if b13 == 1:
            w.opened_box13.configure(image=w._success0)
        if b13 == 2:
            w.opened_box13.configure(image=w._success1)
        if b13 == 3:
            w.opened_box13.configure(image=w._success2)
        if b13 == 4:
            w.opened_box13.configure(image=w._success3)
        if b13 == 5:
            w.opened_box13.configure(image=w._busted)

    def b20_c():
        if b20 == 1:
            w.opened_box20.configure(image=w._success0)
        if b20 == 2:
            w.opened_box20.configure(image=w._success1)
        if b20 == 3:
            w.opened_box20.configure(image=w._success2)
        if b20 == 4:
            w.opened_box20.configure(image=w._success3)
        if b20 == 5:
            w.opened_box20.configure(image=w._busted)

    def b21_c():
        if b21 == 1:
            w.opened_box21.configure(image=w._success0)
        if b21 == 2:
            w.opened_box21.configure(image=w._success1)
        if b21 == 3:
            w.opened_box21.configure(image=w._success2)
        if b21 == 4:
            w.opened_box21.configure(image=w._success3)
        if b21 == 5:
            w.opened_box21.configure(image=w._busted)

    def b22_c():
        if b22 == 1:
            w.opened_box22.configure(image=w._success0)
        if b22 == 2:
            w.opened_box22.configure(image=w._success1)
        if b22 == 3:
            w.opened_box22.configure(image=w._success2)
        if b22 == 4:
            w.opened_box22.configure(image=w._success3)
        if b22 == 5:
            w.opened_box22.configure(image=w._busted)

    def b23_c():
        if b23 == 1:
            w.opened_box23.configure(image=w._success0)
        if b23 == 2:
            w.opened_box23.configure(image=w._success1)
        if b23 == 3:
            w.opened_box23.configure(image=w._success2)
        if b23 == 4:
            w.opened_box23.configure(image=w._success3)
        if b23 == 5:
            w.opened_box23.configure(image=w._busted)

    def b30_c():
        if b30 == 1:
            w.opened_box30.configure(image=w._success0)
        if b30 == 2:
            w.opened_box30.configure(image=w._success1)
        if b30 == 3:
            w.opened_box30.configure(image=w._success2)
        if b30 == 4:
            w.opened_box30.configure(image=w._success3)
        if b30 == 5:
            w.opened_box30.configure(image=w._busted)

    def b31_c():
        if b31 == 1:
            w.opened_box31.configure(image=w._success0)
        if b31 == 2:
            w.opened_box31.configure(image=w._success1)
        if b31 == 3:
            w.opened_box31.configure(image=w._success2)
        if b31 == 4:
            w.opened_box31.configure(image=w._success3)
        if b31 == 5:
            w.opened_box31.configure(image=w._busted)

    def b32_c():
        if b32 == 1:
            w.opened_box32.configure(image=w._success0)
        if b32 == 2:
            w.opened_box32.configure(image=w._success1)
        if b32 == 3:
            w.opened_box32.configure(image=w._success2)
        if b32 == 4:
            w.opened_box32.configure(image=w._success3)
        if b32 == 5:
            w.opened_box32.configure(image=w._busted)

    def b33_c():
        if b33 == 1:
            w.opened_box33.configure(image=w._success0)
        if b33 == 2:
            w.opened_box33.configure(image=w._success1)
        if b33 == 3:
            w.opened_box33.configure(image=w._success2)
        if b33 == 4:
            w.opened_box33.configure(image=w._success3)
        if b33 == 5:
            w.opened_box33.configure(image=w._busted)

    def hide_click(event):
        w.hide.configure(cursor="hand2", background="green")
        b0_c()
        b1_c()
        b2_c()
        b3_c()
        b10_c()
        b11_c()
        b12_c()
        b13_c()
        b20_c()
        b21_c()
        b22_c()
        b23_c()
        b30_c()
        b31_c()
        b32_c()
        b33_c()

    def hide_release(event):
        w.hide.configure(background="#d8d8d8")
        w.opened_box0.configure(image=w._busted1)
        w.opened_box1.configure(image=w._busted2)
        w.opened_box2.configure(image=w._busted3)
        w.opened_box3.configure(image=w._busted4)
        w.opened_box10.configure(image=w._busted11)
        w.opened_box11.configure(image=w._busted12)
        w.opened_box12.configure(image=w._busted13)
        w.opened_box13.configure(image=w._busted14)
        w.opened_box20.configure(image=w._busted21)
        w.opened_box21.configure(image=w._busted22)
        w.opened_box22.configure(image=w._busted23)
        w.opened_box23.configure(image=w._busted24)
        w.opened_box30.configure(image=w._busted31)
        w.opened_box31.configure(image=w._busted32)
        w.opened_box32.configure(image=w._busted33)
        w.opened_box33.configure(image=w._busted34)

    w.hide.bind('<Button-1>', hide_click)
    w.hide.bind('<ButtonRelease-1>', hide_release)
    w.hide.place(x=66, y=708, height=56, width=56)

    busted_box0_cont()
    busted_box1_cont()
    busted_box2_cont()
    busted_box3_cont()
    busted_box10_cont()
    busted_box11_cont()
    busted_box12_cont()
    busted_box13_cont()
    busted_box20_cont()
    busted_box21_cont()
    busted_box22_cont()
    busted_box23_cont()
    busted_box30_cont()
    busted_box31_cont()
    busted_box32_cont()
    busted_box33_cont()
    w.opened_box0.configure(image=w._busted1)
    w.opened_box1.configure(image=w._busted2)
    w.opened_box2.configure(image=w._busted3)
    w.opened_box3.configure(image=w._busted4)
    w.opened_box10.configure(image=w._busted11)
    w.opened_box11.configure(image=w._busted12)
    w.opened_box12.configure(image=w._busted13)
    w.opened_box13.configure(image=w._busted14)
    w.opened_box20.configure(image=w._busted21)
    w.opened_box21.configure(image=w._busted22)
    w.opened_box22.configure(image=w._busted23)
    w.opened_box23.configure(image=w._busted24)
    w.opened_box30.configure(image=w._busted31)
    w.opened_box31.configure(image=w._busted32)
    w.opened_box32.configure(image=w._busted33)
    w.opened_box33.configure(image=w._busted34)
    w.left0.configure(image=w._busted0_left)
    w.left0.place(x=56, y=56)
    w.right0.configure(image=w._busted0_right)
    w.right0.place(x=954, y=56)
    # w.left1.destroy()
    # w.right1.destroy()
    # w.left2.destroy()
    # w.right2.destroy()
    # w.left3.destroy()
    # w.right3.destroy()
    # msg = messagebox.askretrycancel(title="BUSTED", message="You're BUSTED. Try Again?")
    # if msg == True:
    # time.sleep(1)
    # w.re_start()
    # if msg == False:


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

