import sys

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

import tutorial
import level1
import level2
import level3
import level4
import level5
import level6
import level7
import level8
import level9
import level10
import level11
import level12
import level13
import level14
import level15


def select_game():
    global level
    level = w.lvl.get()


def create_game_event():
    if level == 0:
        w.box0.bind('<Double-Button-1>', tutorial.box0_cont)
        w.box1.bind('<Double-Button-1>', tutorial.box1_cont)
        w.box2.bind('<Double-Button-1>', tutorial.box2_cont)
        w.box3.bind('<Double-Button-1>', tutorial.box3_cont)
        w.box10.bind('<Double-Button-1>', tutorial.box10_cont)
        w.box11.bind('<Double-Button-1>', tutorial.box11_cont)
        w.box12.bind('<Double-Button-1>', tutorial.box12_cont)
        w.box13.bind('<Double-Button-1>', tutorial.box13_cont)
        w.box20.bind('<Double-Button-1>', tutorial.box20_cont)
        w.box21.bind('<Double-Button-1>', tutorial.box21_cont)
        w.box22.bind('<Double-Button-1>', tutorial.box22_cont)
        w.box23.bind('<Double-Button-1>', tutorial.box23_cont)
        w.box30.bind('<Double-Button-1>', tutorial.box30_cont)
        w.box31.bind('<Double-Button-1>', tutorial.box31_cont)
        w.box32.bind('<Double-Button-1>', tutorial.box32_cont)
        w.box33.bind('<Double-Button-1>', tutorial.box33_cont)
        tutorial.box_click_control()
        tutorial.list_create()
        def next_click(event):
            w.lvl.set(1)
            w.re_start()
        w.next.bind('<Button-1>', next_click)
        if str(w.lvl1["state"]) == "normal":
            w.next.place(x=1158, y=708, height=54, width=54)
        else:
            w.next.destroy()

    if level == 1:
        w.box0.bind('<Double-Button-1>', level1.box0_cont)
        w.box1.bind('<Double-Button-1>', level1.box1_cont)
        w.box2.bind('<Double-Button-1>', level1.box2_cont)
        w.box3.bind('<Double-Button-1>', level1.box3_cont)
        w.box10.bind('<Double-Button-1>', level1.box10_cont)
        w.box11.bind('<Double-Button-1>', level1.box11_cont)
        w.box12.bind('<Double-Button-1>', level1.box12_cont)
        w.box13.bind('<Double-Button-1>', level1.box13_cont)
        w.box20.bind('<Double-Button-1>', level1.box20_cont)
        w.box21.bind('<Double-Button-1>', level1.box21_cont)
        w.box22.bind('<Double-Button-1>', level1.box22_cont)
        w.box23.bind('<Double-Button-1>', level1.box23_cont)
        w.box30.bind('<Double-Button-1>', level1.box30_cont)
        w.box31.bind('<Double-Button-1>', level1.box31_cont)
        w.box32.bind('<Double-Button-1>', level1.box32_cont)
        w.box33.bind('<Double-Button-1>', level1.box33_cont)
        level1.box_click_control()
        level1.list_create()
        def next_click(event):
            w.lvl.set(2)
            w.re_start()
        w.next.bind('<Button-1>', next_click)
        if str(w.lvl2["state"]) == "normal":
            w.next.place(x=1158, y=708, height=54, width=54)
        else:
            w.next.destroy()

    if level == 2:
        w.box0.bind('<Double-Button-1>', level2.box0_cont)
        w.box1.bind('<Double-Button-1>', level2.box1_cont)
        w.box2.bind('<Double-Button-1>', level2.box2_cont)
        w.box3.bind('<Double-Button-1>', level2.box3_cont)
        w.box10.bind('<Double-Button-1>', level2.box10_cont)
        w.box11.bind('<Double-Button-1>', level2.box11_cont)
        w.box12.bind('<Double-Button-1>', level2.box12_cont)
        w.box13.bind('<Double-Button-1>', level2.box13_cont)
        w.box20.bind('<Double-Button-1>', level2.box20_cont)
        w.box21.bind('<Double-Button-1>', level2.box21_cont)
        w.box22.bind('<Double-Button-1>', level2.box22_cont)
        w.box23.bind('<Double-Button-1>', level2.box23_cont)
        w.box30.bind('<Double-Button-1>', level2.box30_cont)
        w.box31.bind('<Double-Button-1>', level2.box31_cont)
        w.box32.bind('<Double-Button-1>', level2.box32_cont)
        w.box33.bind('<Double-Button-1>', level2.box33_cont)
        level2.box_click_control()
        level2.list_create()
        def next_click(event):
            w.lvl.set(3)
            w.re_start()
        w.next.bind('<Button-1>', next_click)
        if str(w.lvl3["state"]) == "normal":
            w.next.place(x=1158, y=708, height=54, width=54)
        else:
            w.next.destroy()

    if level == 3:
        w.box0.bind('<Double-Button-1>', level3.box0_cont)
        w.box1.bind('<Double-Button-1>', level3.box1_cont)
        w.box2.bind('<Double-Button-1>', level3.box2_cont)
        w.box3.bind('<Double-Button-1>', level3.box3_cont)
        w.box10.bind('<Double-Button-1>', level3.box10_cont)
        w.box11.bind('<Double-Button-1>', level3.box11_cont)
        w.box12.bind('<Double-Button-1>', level3.box12_cont)
        w.box13.bind('<Double-Button-1>', level3.box13_cont)
        w.box20.bind('<Double-Button-1>', level3.box20_cont)
        w.box21.bind('<Double-Button-1>', level3.box21_cont)
        w.box22.bind('<Double-Button-1>', level3.box22_cont)
        w.box23.bind('<Double-Button-1>', level3.box23_cont)
        w.box30.bind('<Double-Button-1>', level3.box30_cont)
        w.box31.bind('<Double-Button-1>', level3.box31_cont)
        w.box32.bind('<Double-Button-1>', level3.box32_cont)
        w.box33.bind('<Double-Button-1>', level3.box33_cont)
        level3.box_click_control()
        level3.list_create()
        def next_click(event):
            w.lvl.set(4)
            w.re_start()
        w.next.bind('<Button-1>', next_click)
        if str(w.lvl4["state"]) == "normal":
            w.next.place(x=1158, y=708, height=54, width=54)
        else:
            w.next.destroy()

    if level == 4:
        w.box0.bind('<Double-Button-1>', level4.box0_cont)
        w.box1.bind('<Double-Button-1>', level4.box1_cont)
        w.box2.bind('<Double-Button-1>', level4.box2_cont)
        w.box3.bind('<Double-Button-1>', level4.box3_cont)
        w.box10.bind('<Double-Button-1>', level4.box10_cont)
        w.box11.bind('<Double-Button-1>', level4.box11_cont)
        w.box12.bind('<Double-Button-1>', level4.box12_cont)
        w.box13.bind('<Double-Button-1>', level4.box13_cont)
        w.box20.bind('<Double-Button-1>', level4.box20_cont)
        w.box21.bind('<Double-Button-1>', level4.box21_cont)
        w.box22.bind('<Double-Button-1>', level4.box22_cont)
        w.box23.bind('<Double-Button-1>', level4.box23_cont)
        w.box30.bind('<Double-Button-1>', level4.box30_cont)
        w.box31.bind('<Double-Button-1>', level4.box31_cont)
        w.box32.bind('<Double-Button-1>', level4.box32_cont)
        w.box33.bind('<Double-Button-1>', level4.box33_cont)
        level4.box_click_control()
        level4.list_create()
        def next_click(event):
            w.lvl.set(5)
            w.re_start()
        w.next.bind('<Button-1>', next_click)
        if str(w.lvl5["state"]) == "normal":
            w.next.place(x=1158, y=708, height=54, width=54)
        else:
            w.next.destroy()

    if level == 5:
        w.box0.bind('<Double-Button-1>', level5.box0_cont)
        w.box1.bind('<Double-Button-1>', level5.box1_cont)
        w.box2.bind('<Double-Button-1>', level5.box2_cont)
        w.box3.bind('<Double-Button-1>', level5.box3_cont)
        w.box10.bind('<Double-Button-1>', level5.box10_cont)
        w.box11.bind('<Double-Button-1>', level5.box11_cont)
        w.box12.bind('<Double-Button-1>', level5.box12_cont)
        w.box13.bind('<Double-Button-1>', level5.box13_cont)
        w.box20.bind('<Double-Button-1>', level5.box20_cont)
        w.box21.bind('<Double-Button-1>', level5.box21_cont)
        w.box22.bind('<Double-Button-1>', level5.box22_cont)
        w.box23.bind('<Double-Button-1>', level5.box23_cont)
        w.box30.bind('<Double-Button-1>', level5.box30_cont)
        w.box31.bind('<Double-Button-1>', level5.box31_cont)
        w.box32.bind('<Double-Button-1>', level5.box32_cont)
        w.box33.bind('<Double-Button-1>', level5.box33_cont)
        level5.box_click_control()
        level5.list_create()
        def next_click(event):
            w.lvl.set(6)
            w.re_start()
        w.next.bind('<Button-1>', next_click)
        if str(w.lvl6["state"]) == "normal":
            w.next.place(x=1158, y=708, height=54, width=54)
        else:
            w.next.destroy()

    if level == 6:
        w.box0.bind('<Double-Button-1>', level6.box0_cont)
        w.box1.bind('<Double-Button-1>', level6.box1_cont)
        w.box2.bind('<Double-Button-1>', level6.box2_cont)
        w.box3.bind('<Double-Button-1>', level6.box3_cont)
        w.box10.bind('<Double-Button-1>', level6.box10_cont)
        w.box11.bind('<Double-Button-1>', level6.box11_cont)
        w.box12.bind('<Double-Button-1>', level6.box12_cont)
        w.box13.bind('<Double-Button-1>', level6.box13_cont)
        w.box20.bind('<Double-Button-1>', level6.box20_cont)
        w.box21.bind('<Double-Button-1>', level6.box21_cont)
        w.box22.bind('<Double-Button-1>', level6.box22_cont)
        w.box23.bind('<Double-Button-1>', level6.box23_cont)
        w.box30.bind('<Double-Button-1>', level6.box30_cont)
        w.box31.bind('<Double-Button-1>', level6.box31_cont)
        w.box32.bind('<Double-Button-1>', level6.box32_cont)
        w.box33.bind('<Double-Button-1>', level6.box33_cont)
        level6.box_click_control()
        level6.list_create()
        def next_click(event):
            w.lvl.set(7)
            w.re_start()
        w.next.bind('<Button-1>', next_click)
        if str(w.lvl7["state"]) == "normal":
            w.next.place(x=1158, y=708, height=54, width=54)
        else:
            w.next.destroy()

    if level == 7:
        w.box0.bind('<Double-Button-1>', level7.box0_cont)
        w.box1.bind('<Double-Button-1>', level7.box1_cont)
        w.box2.bind('<Double-Button-1>', level7.box2_cont)
        w.box3.bind('<Double-Button-1>', level7.box3_cont)
        w.box10.bind('<Double-Button-1>', level7.box10_cont)
        w.box11.bind('<Double-Button-1>', level7.box11_cont)
        w.box12.bind('<Double-Button-1>', level7.box12_cont)
        w.box13.bind('<Double-Button-1>', level7.box13_cont)
        w.box20.bind('<Double-Button-1>', level7.box20_cont)
        w.box21.bind('<Double-Button-1>', level7.box21_cont)
        w.box22.bind('<Double-Button-1>', level7.box22_cont)
        w.box23.bind('<Double-Button-1>', level7.box23_cont)
        w.box30.bind('<Double-Button-1>', level7.box30_cont)
        w.box31.bind('<Double-Button-1>', level7.box31_cont)
        w.box32.bind('<Double-Button-1>', level7.box32_cont)
        w.box33.bind('<Double-Button-1>', level7.box33_cont)
        level7.box_click_control()
        level7.list_create()
        def next_click(event):
            w.lvl.set(8)
            w.re_start()
        w.next.bind('<Button-1>', next_click)
        if str(w.lvl8["state"]) == "normal":
            w.next.place(x=1158, y=708, height=54, width=54)
        else:
            w.next.destroy()

    if level == 8:
        w.box0.bind('<Double-Button-1>', level8.box0_cont)
        w.box1.bind('<Double-Button-1>', level8.box1_cont)
        w.box2.bind('<Double-Button-1>', level8.box2_cont)
        w.box3.bind('<Double-Button-1>', level8.box3_cont)
        w.box10.bind('<Double-Button-1>', level8.box10_cont)
        w.box11.bind('<Double-Button-1>', level8.box11_cont)
        w.box12.bind('<Double-Button-1>', level8.box12_cont)
        w.box13.bind('<Double-Button-1>', level8.box13_cont)
        w.box20.bind('<Double-Button-1>', level8.box20_cont)
        w.box21.bind('<Double-Button-1>', level8.box21_cont)
        w.box22.bind('<Double-Button-1>', level8.box22_cont)
        w.box23.bind('<Double-Button-1>', level8.box23_cont)
        w.box30.bind('<Double-Button-1>', level8.box30_cont)
        w.box31.bind('<Double-Button-1>', level8.box31_cont)
        w.box32.bind('<Double-Button-1>', level8.box32_cont)
        w.box33.bind('<Double-Button-1>', level8.box33_cont)
        level8.box_click_control()
        level8.list_create()
        def next_click(event):
            w.lvl.set(9)
            w.re_start()
        w.next.bind('<Button-1>', next_click)
        if str(w.lvl9["state"]) == "normal":
            w.next.place(x=1158, y=708, height=54, width=54)
        else:
            w.next.destroy()

    if level == 9:
        w.box0.bind('<Double-Button-1>', level9.box0_cont)
        w.box1.bind('<Double-Button-1>', level9.box1_cont)
        w.box2.bind('<Double-Button-1>', level9.box2_cont)
        w.box3.bind('<Double-Button-1>', level9.box3_cont)
        w.box10.bind('<Double-Button-1>', level9.box10_cont)
        w.box11.bind('<Double-Button-1>', level9.box11_cont)
        w.box12.bind('<Double-Button-1>', level9.box12_cont)
        w.box13.bind('<Double-Button-1>', level9.box13_cont)
        w.box20.bind('<Double-Button-1>', level9.box20_cont)
        w.box21.bind('<Double-Button-1>', level9.box21_cont)
        w.box22.bind('<Double-Button-1>', level9.box22_cont)
        w.box23.bind('<Double-Button-1>', level9.box23_cont)
        w.box30.bind('<Double-Button-1>', level9.box30_cont)
        w.box31.bind('<Double-Button-1>', level9.box31_cont)
        w.box32.bind('<Double-Button-1>', level9.box32_cont)
        w.box33.bind('<Double-Button-1>', level9.box33_cont)
        level9.box_click_control()
        level9.list_create()
        def next_click(event):
            w.lvl.set(10)
            w.re_start()
        w.next.bind('<Button-1>', next_click)
        if str(w.lvl10["state"]) == "normal":
            w.next.place(x=1158, y=708, height=54, width=54)
        else:
            w.next.destroy()

    if level == 10:
        w.box0.bind('<Double-Button-1>', level10.box0_cont)
        w.box1.bind('<Double-Button-1>', level10.box1_cont)
        w.box2.bind('<Double-Button-1>', level10.box2_cont)
        w.box3.bind('<Double-Button-1>', level10.box3_cont)
        w.box10.bind('<Double-Button-1>', level10.box10_cont)
        w.box11.bind('<Double-Button-1>', level10.box11_cont)
        w.box12.bind('<Double-Button-1>', level10.box12_cont)
        w.box13.bind('<Double-Button-1>', level10.box13_cont)
        w.box20.bind('<Double-Button-1>', level10.box20_cont)
        w.box21.bind('<Double-Button-1>', level10.box21_cont)
        w.box22.bind('<Double-Button-1>', level10.box22_cont)
        w.box23.bind('<Double-Button-1>', level10.box23_cont)
        w.box30.bind('<Double-Button-1>', level10.box30_cont)
        w.box31.bind('<Double-Button-1>', level10.box31_cont)
        w.box32.bind('<Double-Button-1>', level10.box32_cont)
        w.box33.bind('<Double-Button-1>', level10.box33_cont)
        level10.box_click_control()
        level10.list_create()
        def next_click(event):
            w.lvl.set(11)
            w.re_start()
        w.next.bind('<Button-1>', next_click)
        if str(w.lvl11["state"]) == "normal":
            w.next.place(x=1158, y=708, height=54, width=54)
        else:
            w.next.destroy()

    if level == 11:
        w.box0.bind('<Double-Button-1>', level11.box0_cont)
        w.box1.bind('<Double-Button-1>', level11.box1_cont)
        w.box2.bind('<Double-Button-1>', level11.box2_cont)
        w.box3.bind('<Double-Button-1>', level11.box3_cont)
        w.box10.bind('<Double-Button-1>', level11.box10_cont)
        w.box11.bind('<Double-Button-1>', level11.box11_cont)
        w.box12.bind('<Double-Button-1>', level11.box12_cont)
        w.box13.bind('<Double-Button-1>', level11.box13_cont)
        w.box20.bind('<Double-Button-1>', level11.box20_cont)
        w.box21.bind('<Double-Button-1>', level11.box21_cont)
        w.box22.bind('<Double-Button-1>', level11.box22_cont)
        w.box23.bind('<Double-Button-1>', level11.box23_cont)
        w.box30.bind('<Double-Button-1>', level11.box30_cont)
        w.box31.bind('<Double-Button-1>', level11.box31_cont)
        w.box32.bind('<Double-Button-1>', level11.box32_cont)
        w.box33.bind('<Double-Button-1>', level11.box33_cont)
        level11.box_click_control()
        level11.list_create()
        def next_click(event):
            w.lvl.set(12)
            w.re_start()
        w.next.bind('<Button-1>', next_click)
        if str(w.lvl12["state"]) == "normal":
            w.next.place(x=1158, y=708, height=54, width=54)
        else:
            w.next.destroy()

    if level == 12:
        w.box0.bind('<Double-Button-1>', level12.box0_cont)
        w.box1.bind('<Double-Button-1>', level12.box1_cont)
        w.box2.bind('<Double-Button-1>', level12.box2_cont)
        w.box3.bind('<Double-Button-1>', level12.box3_cont)
        w.box10.bind('<Double-Button-1>', level12.box10_cont)
        w.box11.bind('<Double-Button-1>', level12.box11_cont)
        w.box12.bind('<Double-Button-1>', level12.box12_cont)
        w.box13.bind('<Double-Button-1>', level12.box13_cont)
        w.box20.bind('<Double-Button-1>', level12.box20_cont)
        w.box21.bind('<Double-Button-1>', level12.box21_cont)
        w.box22.bind('<Double-Button-1>', level12.box22_cont)
        w.box23.bind('<Double-Button-1>', level12.box23_cont)
        w.box30.bind('<Double-Button-1>', level12.box30_cont)
        w.box31.bind('<Double-Button-1>', level12.box31_cont)
        w.box32.bind('<Double-Button-1>', level12.box32_cont)
        w.box33.bind('<Double-Button-1>', level12.box33_cont)
        level12.box_click_control()
        level12.list_create()
        def next_click(event):
            w.lvl.set(13)
            w.re_start()
        w.next.bind('<Button-1>', next_click)
        if str(w.lvl13["state"]) == "normal":
            w.next.place(x=1158, y=708, height=54, width=54)
        else:
            w.next.destroy()

    if level == 13:
        w.box0.bind('<Double-Button-1>', level13.box0_cont)
        w.box1.bind('<Double-Button-1>', level13.box1_cont)
        w.box2.bind('<Double-Button-1>', level13.box2_cont)
        w.box3.bind('<Double-Button-1>', level13.box3_cont)
        w.box10.bind('<Double-Button-1>', level13.box10_cont)
        w.box11.bind('<Double-Button-1>', level13.box11_cont)
        w.box12.bind('<Double-Button-1>', level13.box12_cont)
        w.box13.bind('<Double-Button-1>', level13.box13_cont)
        w.box20.bind('<Double-Button-1>', level13.box20_cont)
        w.box21.bind('<Double-Button-1>', level13.box21_cont)
        w.box22.bind('<Double-Button-1>', level13.box22_cont)
        w.box23.bind('<Double-Button-1>', level13.box23_cont)
        w.box30.bind('<Double-Button-1>', level13.box30_cont)
        w.box31.bind('<Double-Button-1>', level13.box31_cont)
        w.box32.bind('<Double-Button-1>', level13.box32_cont)
        w.box33.bind('<Double-Button-1>', level13.box33_cont)
        level13.box_click_control()
        level13.list_create()
        def next_click(event):
            w.lvl.set(14)
            w.re_start()
        w.next.bind('<Button-1>', next_click)
        if str(w.lvl14["state"]) == "normal":
            w.next.place(x=1158, y=708, height=54, width=54)
        else:
            w.next.destroy()

    if level == 14:
        w.box0.bind('<Double-Button-1>', level14.box0_cont)
        w.box1.bind('<Double-Button-1>', level14.box1_cont)
        w.box2.bind('<Double-Button-1>', level14.box2_cont)
        w.box3.bind('<Double-Button-1>', level14.box3_cont)
        w.box10.bind('<Double-Button-1>', level14.box10_cont)
        w.box11.bind('<Double-Button-1>', level14.box11_cont)
        w.box12.bind('<Double-Button-1>', level14.box12_cont)
        w.box13.bind('<Double-Button-1>', level14.box13_cont)
        w.box20.bind('<Double-Button-1>', level14.box20_cont)
        w.box21.bind('<Double-Button-1>', level14.box21_cont)
        w.box22.bind('<Double-Button-1>', level14.box22_cont)
        w.box23.bind('<Double-Button-1>', level14.box23_cont)
        w.box30.bind('<Double-Button-1>', level14.box30_cont)
        w.box31.bind('<Double-Button-1>', level14.box31_cont)
        w.box32.bind('<Double-Button-1>', level14.box32_cont)
        w.box33.bind('<Double-Button-1>', level14.box33_cont)
        level14.box_click_control()
        level14.list_create()
        def next_click(event):
            w.lvl.set(15)
            w.re_start()
        w.next.bind('<Button-1>', next_click)
        if str(w.lvl15["state"]) == "normal":
            w.next.place(x=1158, y=708, height=54, width=54)
        else:
            w.next.destroy()

    if level == 15:
        w.box0.bind('<Double-Button-1>', level15.box0_cont)
        w.box1.bind('<Double-Button-1>', level15.box1_cont)
        w.box2.bind('<Double-Button-1>', level15.box2_cont)
        w.box3.bind('<Double-Button-1>', level15.box3_cont)
        w.box10.bind('<Double-Button-1>', level15.box10_cont)
        w.box11.bind('<Double-Button-1>', level15.box11_cont)
        w.box12.bind('<Double-Button-1>', level15.box12_cont)
        w.box13.bind('<Double-Button-1>', level15.box13_cont)
        w.box20.bind('<Double-Button-1>', level15.box20_cont)
        w.box21.bind('<Double-Button-1>', level15.box21_cont)
        w.box22.bind('<Double-Button-1>', level15.box22_cont)
        w.box23.bind('<Double-Button-1>', level15.box23_cont)
        w.box30.bind('<Double-Button-1>', level15.box30_cont)
        w.box31.bind('<Double-Button-1>', level15.box31_cont)
        w.box32.bind('<Double-Button-1>', level15.box32_cont)
        w.box33.bind('<Double-Button-1>', level15.box33_cont)
        level15.box_click_control()
        level15.list_create()
        w.next.destroy()


def start_game():
    select_game()
    create_game_event()

def init(app, gui, *args, **kwargs):
    global w, root
    w = gui
    root = app

