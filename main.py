import sys
import time
import main_support
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
from PIL import Image, ImageTk
from itertools import count
from tkinter import messagebox


try:
    import Tkinter as tk
except:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True


class ImageLabel(tk.Label):
    def __init__(self, master, *args, **kwargs):
        tk.Label.__init__(self, master, *args, **kwargs)
        self.configure(borderwidth="0")

    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)


class HighlightLabel(tk.Label):

    def __init__(self, master, *args, **kwargs):
        tk.Label.__init__(self, master, *args, **kwargs)
        self.configure(bg="#741B27",highlightcolor="#B9283C",borderwidth="0")
        self._bg = self['bg']
        self._bg = "#741B27"
        self.bind('<Enter>', self._on_enter)
        self.bind('<Leave>', self._on_leave)

    def _on_enter(self, event):
        self.configure(bg=self['highlightcolor'],cursor="hand2")

    def _on_leave(self, event):
        self.configure(bg=self._bg)

class HighlightForegroundLabel(tk.Label):

    def __init__(self, master, *args, **kwargs):
        tk.Label.__init__(self, master, *args, **kwargs)
        self.configure(foreground="white",borderwidth="0")
        self.bind('<Enter>', self._on_enter)
        self.bind('<Leave>', self._on_leave)

    def _on_enter(self, event):
        self.configure(foreground="green",cursor="hand2")

    def _on_leave(self, event):
        self.configure(foreground="white")


def start_gui():
    global root
    root = tk.Tk()
    app = GameofHackerapp(root)
    main_support.init(root,app)
    tutorial.init(root, app)
    level1.init(root, app)
    level2.init(root, app)
    level3.init(root, app)
    level4.init(root, app)
    level5.init(root, app)
    level6.init(root, app)
    level7.init(root, app)
    level8.init(root, app)
    level9.init(root, app)
    level10.init(root, app)
    level11.init(root, app)
    level12.init(root, app)
    level13.init(root, app)
    level14.init(root, app)
    level15.init(root, app)
    root.mainloop()


class GameofHackerapp:
    def __init__(self, app=None):

        app.geometry("1264x960+328+40")
        app.title("Game of Hacker")
        app.wm_attributes('-topmost', 1)
        app.resizable(False, False)

        def _light_on(event):
            self.goh1.place_forget()
            self.goh2.place(x=606, y=0, height=52, width=52)
            self.web_cam_txt.place(x=520, y=0, height=52, width=230)

        def _light_off(event):
            self.goh2.place_forget()
            self.goh1.place(x=606, y=0, height=52, width=52)
            self.web_cam_txt.place_forget()

        self._monitor = tk.PhotoImage(file="img/main/monitor.png")
        self._turn_on = tk.PhotoImage(file="img/main/turn_on.png")
        self._turn_off = tk.PhotoImage(file="img/main/turn_off.png")
        self._goh1 = tk.PhotoImage(file="img/main/goh_no_light.png")
        self._goh2 = tk.PhotoImage(file="img/main/goh_light.png")

        self.l1 = 0
        self.m1 = 0
        self.gb = 0
        self.b1 = 0
        self.i1 = 0
        self.eng = 1
        self.trk = 0
        self.lvl = tk.IntVar()
        self.lvl.set(0)

        self.monitor = tk.Label(app)
        self.monitor.configure(image=self._monitor, bg="black")
        self.monitor.place(x=0, y=0, height=960, width=1264)
        self.web_cam_txt = tk.Label(app)
        self.web_cam_txt.configure(background="#282828", borderwidth="0", foreground="#008000", font="-family {Segoe UI} -size 14 -weight bold", text='''YOUR                   ACTIVE''')
        self.web_cam_txt.place(x=520, y=0, height=52, width=230)
        self.web_cam_txt.place_forget()
        self.goh1 = tk.Label(app)
        self.goh1.configure(image=self._goh1,cursor="hand2")
        self.goh1.place(x=606,y=0,height=52,width=52)
        self.goh1.bind('<Enter>', _light_on)
        self.goh2 = tk.Label(app)
        self.goh2.configure(image=self._goh2,cursor="hand2")
        self.goh2.bind('<Leave>', _light_off)

        self.open_turn_on()
        self.create_bg()
        self.create_menu()
        self.create_menu_level()
        self.create_menu_info()
        self.create_images()

    def open_turn_on(self):
        def _open_click(event):
            self.turn_on.destroy()
            self.open_turn_off()
            if self.b1 == 0:
                self.background_open()
            if self.m1 == 0:
                self.menu_open()
            if self.l1 == 1:
                self.level_close()
            if self.gb == 1:
                self.game_box_close()
            if self.i1 == 1:
                self.info_close()

        self.turn_on = tk.Label()
        self.turn_on.configure(image=self._turn_on, cursor="hand2", bg="#282828")
        self.turn_on.place(x=606, y=710, height=52, width=52)
        self.turn_on.bind('<Button-1>', _open_click)

    def open_turn_off(self):
        def _close_click(event):
            #self.next.destroy()
            self.turn_off.destroy()
            self.open_turn_on()
            if self.b1 == 1:
                #self.create_bg()
                self.background_close()
            if self.m1 == 1:
                #self.create_menu()
                self.menu_close()
            if self.l1 == 1:
                self.level_close()
            if self.gb == 1:
                self.game_box_close()
            if self.i1 == 1:
                self.info_close()

        self.turn_off = tk.Label()
        self.turn_off.configure(image=self._turn_off, cursor="hand2", bg="#282828")
        self.turn_off.place(x=606, y=710, height=52, width=52)
        self.turn_off.bind('<Button-1>', _close_click)

    def create_bg(self, app=None):
        self.back_ground0 = ImageLabel(app)
        self.back_ground0.load("img/bg/top-left.gif")
        self.back_ground0.place(x=54, y=54, height=268, width=414)
        self.back_ground0.place_forget()
        self.back_ground1 = ImageLabel(app)
        self.back_ground1.load("img/bg/top-center.gif")
        self.back_ground1.place(x=800, y=54, height=268, width=414)
        self.back_ground1.place_forget()
        self.back_ground10 = ImageLabel(app)
        self.back_ground10.load("img/bg/top-center.gif")
        self.back_ground10.place(x=54, y=322, height=268, width=414)
        self.back_ground10.place_forget()
        self.back_ground11 = ImageLabel(app)
        self.back_ground11.load("img/bg/top-left.gif")
        self.back_ground11.place(x=800, y=322, height=268, width=414)
        self.back_ground11.place_forget()
        self.back_ground20 = ImageLabel(app)
        self.back_ground20.load("img/bg/top-center.gif")
        self.back_ground20.place(x=54, y=590, height=108, width=414)
        self.back_ground20.place_forget()
        self.back_ground21 = ImageLabel(app)
        self.back_ground21.load("img/bg/top-center.gif")
        self.back_ground21.place(x=800, y=590, height=108, width=414)
        self.back_ground21.place_forget()
        self.b_t = ImageLabel(app)
        self.b_t.load("img/bg/top-left.gif")
        self.b_t.place(x=468, y=54, height=46, width=332)
        self.b_t.place_forget()
        self.b_b = ImageLabel(app)
        self.b_b.load("img/bg/top-left.gif")
        self.b_b.place(x=468, y=650, height=55, width=332)
        self.b_b.place_forget()

    def background_open(self):
        self.b1 = 1
        self.back_ground0.place(x=54, y=54, height=268, width=414)
        self.back_ground1.place(x=800, y=54, height=268, width=414)
        self.back_ground10.place(x=54, y=322, height=268, width=414)
        self.back_ground11.place(x=800, y=322, height=268, width=414)
        self.back_ground20.place(x=54, y=590, height=108, width=414)
        self.back_ground21.place(x=800, y=590, height=108, width=414)
        self.b_t.place(x=468, y=54, height=46, width=332)
        self.b_b.place(x=468, y=650, height=55, width=332)

    def background_close(self):
        self.b1 = 0
        self.back_ground0.place_forget()
        self.back_ground1.place_forget()
        self.back_ground10.place_forget()
        self.back_ground11.place_forget()
        self.back_ground20.place_forget()
        self.back_ground21.place_forget()
        self.b_t.place_forget()
        self.b_b.place_forget()

    def create_menu(self, app=None):
        def _menu_start(event):
            if self.b1 == 1:
                self.background_close()
            if self.gb == 0:
                self.game_box_create()
                main_support.start_game()
            if self.m1 == 1:
                self.menu_close()
            if self.l1 == 1:
                self.level_close()
            if self.i1 == 1:
                self.info_close()

        def _menu_level(event):
            if self.m1 == 1:
                self.menu_close()
            if self.i1 == 1:
                self.info_close()
            self.background_close()
            self.level_open()

        def _menu_info(event):
            if self.m1 == 1:
                self.menu_close()
            self.background_close()
            self.info_open()

        def _exit(event):
            msg = messagebox.showwarning(title="Your progress will be deleted.", message="If you quit the game, all your progress will be DELETED!")
            if msg == "ok":
                msg2 = messagebox.askyesno(title="EXIT?", message="Are you sure?")
                if msg2 == True:
                    root.destroy()

        self.game_start_button = HighlightForegroundLabel(app, background="#1B1A2D", foreground="#ffffff", font="-family {Segoe UI} -size 20 -weight bold", text="START GAME")
        self.game_start_button.bind('<Button-1>', _menu_start)
        self.game_level_button = HighlightForegroundLabel(app, background="#24223C", foreground="#ffffff", font="-family {Segoe UI} -size 20 -weight bold", text="LEVELS")
        self.game_level_button.bind('<Button-1>', _menu_level)
        self.game_info_button = HighlightForegroundLabel(app, background="#19172A", foreground="#ffffff", font="-family {Segoe UI} -size 20 -weight bold", text="INFORMATIONS")
        self.game_info_button.bind('<Button-1>', _menu_info)
        self.game_exit_button = HighlightForegroundLabel(app, background="#222222", foreground="#ffffff", font="-family {Segoe UI} -size 20 -weight bold", text="EXIT")
        self.game_exit_button.bind('<Button-1>', _exit)

    def menu_open(self):
        self.m1 = 1
        self.game_start_button.place(x=468, y=100, height=130, width=332)
        self.game_level_button.place(x=468, y=240, height=130, width=332)
        self.game_info_button.place(x=468, y=380, height=130, width=332)
        self.game_exit_button.place(x=468, y=520, height=130, width=332)

    def menu_close(self):
        self.m1 = 0
        self.game_start_button.place_forget()
        self.game_level_button.place_forget()
        self.game_info_button.place_forget()
        self.game_exit_button.place_forget()

        # MENU - LEVELS - BUTTONS

    def create_menu_level(self, app=None):
        def _level_back(event):
            if self.l1 == 1:
                self.level_close()
            if self.m1 == 0:
                self.menu_open()
            if self.b1 == 0:
                self.background_open()
            if self.i1 == 1:
                self.info_close()
        self.level_back_button = HighlightForegroundLabel(app, background="#222222", foreground="#ffffff", font="-family {Segoe UI} -size 20 -weight bold", text="BACK")
        self.level_back_button.bind('<Button-1>', _level_back)
        self.lvl1txt = tk.Label(app, font="-family {Segoe UI} -size 20 -weight bold", text="LAMER 1           ")
        self.lv2txt = tk.Label(app, font="-family {Segoe UI} -size 20 -weight bold", text="           LAMER 2")
        self.lvl3txt = tk.Label(app, font="-family {Segoe UI} -size 18 -weight bold", text="SCRIPT KIDDIE 1  ")
        self.lvl4txt = tk.Label(app, font="-family {Segoe UI} -size 18 -weight bold", text="  SCRIPT KIDDIE 2")
        self.lvl5txt = tk.Label(app, font="-family {Segoe UI} -size 20 -weight bold", text="PHREAKER 1       ")
        self.lvl6txt = tk.Label(app, font="-family {Segoe UI} -size 20 -weight bold", text="       PHREAKER 2")
        self.lvl7txt = tk.Label(app, font="-family {Segoe UI} -size 20 -weight bold", text="CRACKER 1         ")
        self.lvl8txt = tk.Label(app, font="-family {Segoe UI} -size 20 -weight bold", text="         CRACKER 2")
        self.lvl9txt = tk.Label(app, font="-family {Segoe UI} -size 20 -weight bold", text="HACKTIVIST 1    ")
        self.lvl0txt = tk.Label(app, font="-family {Segoe UI} -size 20 -weight bold", text="    HACKTIVIST 2")
        self.lvl11txt = tk.Label(app, font="-family {Segoe UI} -size 20 -weight bold", text="GREY HAT 1        ")
        self.lvl12txt = tk.Label(app, font="-family {Segoe UI} -size 20 -weight bold", text="        GREY HAT 2")
        self.lvl13txt = tk.Label(app, font="-family {Segoe UI} -size 20 -weight bold", text="BLACK HAT 1      ")
        self.lvl14txt = tk.Label(app, font="-family {Segoe UI} -size 20 -weight bold", text="      BLACK HAT 2")
        self.lvl15txt = tk.Label(app, font="-family {Segoe UI} -size 20 -weight bold", text="   WHITE HAT")
        self.lvl1 = tk.Radiobutton(app, variable=self.lvl, value=1, state="disabled")
        self.lvl2 = tk.Radiobutton(app, variable=self.lvl, value=2, state="disabled")
        self.lvl3 = tk.Radiobutton(app, variable=self.lvl, value=3, state="disabled")
        self.lvl4 = tk.Radiobutton(app, variable=self.lvl, value=4, state="disabled")
        self.lvl5 = tk.Radiobutton(app, variable=self.lvl, value=5, state="disabled")
        self.lvl6 = tk.Radiobutton(app, variable=self.lvl, value=6, state="disabled")
        self.lvl7 = tk.Radiobutton(app, variable=self.lvl, value=7, state="disabled")
        self.lvl8 = tk.Radiobutton(app, variable=self.lvl, value=8, state="disabled")
        self.lvl9 = tk.Radiobutton(app, variable=self.lvl, value=9, state="disabled")
        self.lvl10 = tk.Radiobutton(app, variable=self.lvl, value=10, state="disabled")
        self.lvl11 = tk.Radiobutton(app, variable=self.lvl, value=11, state="disabled")
        self.lvl12 = tk.Radiobutton(app, variable=self.lvl, value=12, state="disabled")
        self.lvl13 = tk.Radiobutton(app, variable=self.lvl, value=13, state="disabled")
        self.lvl14 = tk.Radiobutton(app, variable=self.lvl, value=14, state="disabled")
        self.lvl15 = tk.Radiobutton(app, variable=self.lvl, value=15, state="disabled")

        # MENU BACKGROUND LIVe

    def level_open(self):
        self.l1 = 1
        self.level_back_button.place(x=468, y=60, height=80, width=332)
        self.lvl1txt.place(x=418, y=160, width=214, height=25)
        self.lv2txt.place(x=632, y=160, width=214, height=25)
        self.lvl3txt.place(x=418, y=230, width=214, height=25)
        self.lvl4txt.place(x=632, y=230, width=214, height=25)
        self.lvl5txt.place(x=418, y=300, width=214, height=25)
        self.lvl6txt.place(x=632, y=300, width=214, height=25)
        self.lvl7txt.place(x=418, y=370, width=214, height=25)
        self.lvl8txt.place(x=632, y=370, width=214, height=25)
        self.lvl9txt.place(x=418, y=440, width=214, height=25)
        self.lvl0txt.place(x=632, y=440, width=214, height=25)
        self.lvl11txt.place(x=418, y=510, width=214, height=25)
        self.lvl12txt.place(x=632, y=510, width=214, height=25)
        self.lvl13txt.place(x=418, y=580, width=214, height=25)
        self.lvl14txt.place(x=632, y=580, width=214, height=25)
        self.lvl15txt.place(x=525, y=650, width=214, height=25)
        self.lvl1.place(x=390, y=160, width=28, height=25)
        self.lvl2.place(x=846, y=160, width=28, height=25)
        self.lvl3.place(x=390, y=230, width=28, height=25)
        self.lvl4.place(x=846, y=230, width=28, height=25)
        self.lvl5.place(x=390, y=300, width=28, height=25)
        self.lvl6.place(x=846, y=300, width=28, height=25)
        self.lvl7.place(x=390, y=370, width=28, height=25)
        self.lvl8.place(x=846, y=370, width=28, height=25)
        self.lvl9.place(x=390, y=440, width=28, height=25)
        self.lvl10.place(x=846, y=440, width=28, height=25)
        self.lvl11.place(x=390, y=510, width=28, height=25)
        self.lvl12.place(x=846, y=510, width=28, height=25)
        self.lvl13.place(x=390, y=580, width=28, height=25)
        self.lvl14.place(x=846, y=580, width=28, height=25)
        self.lvl15.place(x=739, y=650, width=28, height=25)

    def level_close(self):
        self.l1 = 0
        self.level_back_button.place_forget()
        self.lvl1txt.place_forget()
        self.lvl1txt.place_forget()
        self.lv2txt.place_forget()
        self.lvl3txt.place_forget()
        self.lvl4txt.place_forget()
        self.lvl5txt.place_forget()
        self.lvl6txt.place_forget()
        self.lvl7txt.place_forget()
        self.lvl8txt.place_forget()
        self.lvl9txt.place_forget()
        self.lvl0txt.place_forget()
        self.lvl11txt.place_forget()
        self.lvl12txt.place_forget()
        self.lvl13txt.place_forget()
        self.lvl14txt.place_forget()
        self.lvl15txt.place_forget()
        self.lvl1.place_forget()
        self.lvl2.place_forget()
        self.lvl3.place_forget()
        self.lvl4.place_forget()
        self.lvl5.place_forget()
        self.lvl6.place_forget()
        self.lvl7.place_forget()
        self.lvl8.place_forget()
        self.lvl9.place_forget()
        self.lvl10.place_forget()
        self.lvl11.place_forget()
        self.lvl12.place_forget()
        self.lvl13.place_forget()
        self.lvl14.place_forget()
        self.lvl15.place_forget()

        # MENU BUTTONS

    def create_menu_info(self, app=None):
        def en_click(event):
            self.trk = 0
            self.eng = 1
            self.tr.configure(foreground="gray")
            self.en.configure(foreground="red")
            self.trmsg1.place_forget()
            self.trmsg11.place_forget()
            self.trmsg2.place_forget()
            self.trmsg21.place_forget()
            self.trmsg3.place_forget()
            self.trmsg31.place_forget()
            self.enmsg1.place(x=430, y=170, width=430, height=35)
            self.enmsg11.place(x=430,y=210, width=430, height=35)
            self.enmsg2.place(x=430, y=280, width=430, height=35)
            self.enmsg21.place(x=430, y=320, width=430, height=35)
            self.enmsg3.place(x=430, y=390, width=450, height=40)
            self.enmsg31.place(x=430, y=430, width=430, height=40)


        def tr_click(event):
            self.trk = 1
            self.eng = 0
            self.en.configure(foreground="gray")
            self.tr.configure(foreground="red")
            self.enmsg1.place_forget()
            self.enmsg11.place_forget()
            self.enmsg2.place_forget()
            self.enmsg21.place_forget()
            self.enmsg3.place_forget()
            self.enmsg31.place_forget()
            self.trmsg1.place(x=430, y=170, width=430, height=35)
            self.trmsg11.place(x=430, y=210, width=430, height=35)
            self.trmsg2.place(x=430, y=280, width=430, height=35)
            self.trmsg21.place(x=430, y=320, width=430, height=35)
            self.trmsg3.place(x=430, y=390, width=450, height=40)
            self.trmsg31.place(x=430, y=430, width=430, height=40)

        self.en = tk.Label(app, font="-family {Segoe UI} -size 24 -weight bold", bg="black", foreground="red", cursor="hand2", text="EN")
        self.en.bind('<Button-1>', en_click)
        self.dot = tk.Label(app, font="-family {Segoe UI} -size 24 -weight bold", bg="black", foreground="gray", text="/")
        self.tr = tk.Label(app, font="-family {Segoe UI} -size 24 -weight bold", bg="black", foreground="gray", cursor="hand2", text="TR")
        self.tr.bind('<Button-1>',tr_click)
        self.enmsg1 = tk.Label(app, font="-family {Segoe UI} -size 20 -weight normal", bg="black", foreground="gray", text="If you want to hack something you")
        self.enmsg11 = tk.Label(app, font="-family {Segoe UI} -size 20 -weight normal", bg="black", foreground="gray", text=" have to <double left click>.")
        self.enmsg2 = tk.Label(app, font="-family {Segoe UI} -size 20 -weight bold", bg="black", foreground="gray", text="One mouse click is just")
        self.enmsg21 = tk.Label(app, font="-family {Segoe UI} -size 20 -weight bold", bg="black", foreground="gray", text=" writing code...")
        self.enmsg3 = tk.Label(app, font="-family {Segoe UI} -size 20 -weight normal", bg="black", foreground="gray", text="Remember that you can't always win. ")
        self.enmsg31 = tk.Label(app, font="-family {Segoe UI} -size 20 -weight normal", bg="black", foreground="gray", text="Be patient and finish the game!")
        self.trmsg1 = tk.Label(app, font="-family {Segoe UI} -size 20 -weight normal", bg="black", foreground="gray", text="Bir şeyler hacklemek istiyorsan")
        self.trmsg11 = tk.Label(app, font="-family {Segoe UI} -size 20 -weight normal", bg="black", foreground="gray", text="iki kere sol tıklamalısın.")
        self.trmsg2 = tk.Label(app, font="-family {Segoe UI} -size 20 -weight bold", bg="black", foreground="gray", text="Bir kere tıkladığında sadece")
        self.trmsg21 = tk.Label(app, font="-family {Segoe UI} -size 20 -weight bold", bg="black", foreground="gray", text="kod yazar...")
        self.trmsg3 = tk.Label(app, font="-family {Segoe UI} -size 20 -weight normal", bg="black", foreground="gray", text="Her zaman kazanamayacağını unutma.")
        self.trmsg31 = tk.Label(app, font="-family {Segoe UI} -size 20 -weight normal", bg="black", foreground="gray", text="Sabırlı ol ve oyunu bitir!")
        self.cr = tk.Label(app, font="-family {Segoe UI} -size 14 -weight normal", bg="black", foreground="gray", text="created by.")
        self.ek = tk.Label(app, font="-family {Segoe UI} -size 14 -weight bold", bg="black", foreground="gray", text="M.Enes KAYA")

    def info_open(self):
        self.i1 = 1
        self.en.place(x=880, y=70, width=44, height=31)
        self.dot.place(x=922, y=70, width=24, height=31)
        self.tr.place(x=944, y=70, width=44, height=31)
        self.cr.place(x=740, y=580, width=210, height=33)
        self.ek.place(x=730, y=610, width=220, height=33)
        if self.trk == 1:
            self.trmsg1.place(x=430, y=170, width=430, height=35)
            self.trmsg11.place(x=430, y=210, width=430, height=35)
            self.trmsg2.place(x=430, y=280, width=430, height=35)
            self.trmsg21.place(x=430, y=320, width=430, height=35)
            self.trmsg3.place(x=430, y=390, width=450, height=40)
            self.trmsg31.place(x=430, y=430, width=430, height=40)
        if self.eng == 1:
            self.enmsg1.place(x=430, y=170, width=430, height=35)
            self.enmsg11.place(x=430,y=210, width=430, height=35)
            self.enmsg2.place(x=430, y=280, width=430, height=35)
            self.enmsg21.place(x=430, y=320, width=430, height=35)
            self.enmsg3.place(x=430, y=390, width=450, height=40)
            self.enmsg31.place(x=430, y=430, width=430, height=40)


    def info_close(self):
        self.i1 = 0
        self.en.place_forget()
        self.dot.place_forget()
        self.tr.place_forget()
        self.enmsg1.place_forget()
        self.enmsg11.place_forget()
        self.enmsg2.place_forget()
        self.enmsg21.place_forget()
        self.enmsg3.place_forget()
        self.enmsg31.place_forget()
        self.trmsg1.place_forget()
        self.trmsg11.place_forget()
        self.trmsg2.place_forget()
        self.trmsg21.place_forget()
        self.trmsg3.place_forget()
        self.trmsg31.place_forget()
        self.cr.place_forget()
        self.ek.place_forget()

    def game_box_create(self, app=None):
        self._anim = ImageLabel(app)
        self._anim.load("img/hacking/hacking.gif")
        # BOX - 0
        def box_press0(event):
            self.box0.place_forget()
            self._anim.place(x=306, y=56, height=160, width=160)
        def box_release0(event):
            self._anim.place_forget()
            self.box0.place(x=306, y=56, height=160, width=160)
        self.opened_box0 = tk.Label(app, borderwidth="0")
        self.box0 = HighlightLabel(app)
        self.box0.bind('<Button-1>', box_press0)
        self.box0.bind('<ButtonRelease-1>', box_release0)
        # BOX - 1
        def box_press1(event):
            self.box1.place_forget()
            self._anim.place(x=468, y=56, height=160, width=160)
        def box_release1(event):
            self._anim.place_forget()
            self.box1.place(x=468, y=56, height=160, width=160)
        self.opened_box1 = tk.Label(app, borderwidth="0")
        self.box1 = HighlightLabel(app)
        self.box1.bind('<Button-1>', box_press1)
        self.box1.bind('<ButtonRelease-1>', box_release1)
        # BOX - 2
        def box_press2(event):
            self.box2.place_forget()
            self._anim.place(x=630, y=56, height=160, width=160)
        def box_release2(event):
            self._anim.place_forget()
            self.box2.place(x=630, y=56, height=160, width=160)
        self.opened_box2 = tk.Label(app, borderwidth="0")
        self.box2 = HighlightLabel(app)
        self.box2.bind('<Button-1>', box_press2)
        self.box2.bind('<ButtonRelease-1>', box_release2)
        # BOX - 3
        def box_press3(event):
            self.box3.place_forget()
            self._anim.place(x=792, y=56, height=160, width=160)
        def box_release3(event):
            self._anim.place_forget()
            self.box3.place(x=792, y=56, height=160, width=160)
        self.opened_box3 = tk.Label(app, borderwidth="0")
        self.box3 = HighlightLabel(app)
        self.box3.bind('<Button-1>', box_press3)
        self.box3.bind('<ButtonRelease-1>', box_release3)
        # BOX - 10
        def box_press10(event):
            self.box10.place_forget()
            self._anim.place(x=306, y=218, height=160, width=160)
        def box_release10(event):
            self._anim.place_forget()
            self.box10.place(x=306, y=218, height=160, width=160)
        self.opened_box10 = tk.Label(app, borderwidth="0")
        self.box10 = HighlightLabel(app)
        self.box10.bind('<Button-1>', box_press10)
        self.box10.bind('<ButtonRelease-1>', box_release10)
        # BOX - 11
        def box_press11(event):
            self.box11.place_forget()
            self._anim.place(x=468, y=218, height=160, width=160)
        def box_release11(event):
            self._anim.place_forget()
            self.box11.place(x=468, y=218, height=160, width=160)
        self.opened_box11 = tk.Label(app, borderwidth="0")
        self.box11 = HighlightLabel(app)
        self.box11.bind('<Button-1>', box_press11)
        self.box11.bind('<ButtonRelease-1>', box_release11)
        # BOX - 12
        def box_press12(event):
            self.box12.place_forget()
            self._anim.place(x=630, y=218, height=160, width=160)
        def box_release12(event):
            self._anim.place_forget()
            self.box12.place(x=630, y=218, height=160, width=160)
        self.opened_box12 = tk.Label(app, borderwidth="0")
        self.box12 = HighlightLabel(app)
        self.box12.bind('<Button-1>', box_press12)
        self.box12.bind('<ButtonRelease-1>', box_release12)
        # BOX - 13
        def box_press13(event):
            self.box13.place_forget()
            self._anim.place(x=792, y=218, height=160, width=160)
        def box_release13(event):
            self._anim.place_forget()
            self.box13.place(x=792, y=218, height=160, width=160)
        self.opened_box13 = tk.Label(app, borderwidth="0")
        self.box13 = HighlightLabel(app)
        self.box13.bind('<Button-1>', box_press13)
        self.box13.bind('<ButtonRelease-1>', box_release13)
        # BOX - 20
        def box_press20(event):
            self.box20.place_forget()
            self._anim.place(x=306, y=380, height=160, width=160)
        def box_release20(event):
            self._anim.place_forget()
            self.box20.place(x=306, y=380, height=160, width=160)
        self.opened_box20 = tk.Label(app, borderwidth="0")
        self.box20 = HighlightLabel(app)
        self.box20.bind('<Button-1>', box_press20)
        self.box20.bind('<ButtonRelease-1>', box_release20)
        # BOX - 21
        def box_press21(event):
            self.box21.place_forget()
            self._anim.place(x=468, y=380, height=160, width=160)
        def box_release21(event):
            self._anim.place_forget()
            self.box21.place(x=468, y=380, height=160, width=160)
        self.opened_box21 = tk.Label(app, borderwidth="0")
        self.box21 = HighlightLabel(app)
        self.box21.bind('<Button-1>', box_press21)
        self.box21.bind('<ButtonRelease-1>', box_release21)
        # BOX - 22
        def box_press22(event):
            self.box22.place_forget()
            self._anim.place(x=630, y=380, height=160, width=160)
        def box_release22(event):
            self._anim.place_forget()
            self.box22.place(x=630, y=380, height=160, width=160)
        self.opened_box22 = tk.Label(app, borderwidth="0")
        self.box22 = HighlightLabel(app)
        self.box22.bind('<Button-1>', box_press22)
        self.box22.bind('<ButtonRelease-1>', box_release22)
        # BOX - 23
        def box_press23(event):
            self.box23.place_forget()
            self._anim.place(x=792, y=380, height=160, width=160)
        def box_release23(event):
            self._anim.place_forget()
            self.box23.place(x=792, y=380, height=160, width=160)
        self.opened_box23 = tk.Label(app, borderwidth="0")
        self.box23 = HighlightLabel(app)
        self.box23.bind('<Button-1>', box_press23)
        self.box23.bind('<ButtonRelease-1>', box_release23)
        # BOX - 30
        def box_press30(event):
            self.box30.place_forget()
            self._anim.place(x=306, y=542, height=160, width=160)
        def box_release30(event):
            self._anim.place_forget()
            self.box30.place(x=306, y=542, height=160, width=160)
        self.opened_box30 = tk.Label(app, borderwidth="0")
        self.box30 = HighlightLabel(app)
        self.box30.bind('<Button-1>', box_press30)
        self.box30.bind('<ButtonRelease-1>', box_release30)
        # BOX - 31
        def box_press31(event):
            self.box31.place_forget()
            self._anim.place(x=468, y=542, height=160, width=160)
        def box_release31(event):
            self._anim.place_forget()
            self.box31.place(x=468, y=542, height=160, width=160)
        self.opened_box31 = tk.Label(app, borderwidth="0")
        self.box31 = HighlightLabel(app)
        self.box31.bind('<Button-1>', box_press31)
        self.box31.bind('<ButtonRelease-1>', box_release31)
        # BOX - 32
        def box_press32(event):
            self.box32.place_forget()
            self._anim.place(x=630, y=542, height=160, width=160)
        def box_release32(event):
            self._anim.place_forget()
            self.box32.place(x=630, y=542, height=160, width=160)
        self.opened_box32 = tk.Label(app, borderwidth="0")
        self.box32 = HighlightLabel(app)
        self.box32.bind('<Button-1>', box_press32)
        self.box32.bind('<ButtonRelease-1>', box_release32)
        # BOX - 33
        def box_press33(event):
            self.box33.place_forget()
            self._anim.place(x=792, y=542, height=160, width=160)
        def box_release33(event):
            self._anim.place_forget()
            self.box33.place(x=792, y=542, height=160, width=160)
        self.opened_box33 = tk.Label(app, borderwidth="0")
        self.box33 = HighlightLabel(app)
        self.box33.bind('<Button-1>', box_press33)
        self.box33.bind('<ButtonRelease-1>', box_release33)
        # SIDE
        self.left0 = tk.Label(app, borderwidth="0")
        self.right0 = tk.Label(app, borderwidth="0")
        # RETRY - NEXT - MENU - HIDE
        def hide_enter(event):
            self.hide.configure(cursor="hand2")
        def hide_leave(event):
            self.hide.configure(background="#d8d8d8")
        self.hide = tk.Label(app, borderwidth="0", background="#d8d8d8", image=self._hide0)
        self.hide.bind('<Enter>', hide_enter)
        self.hide.bind('<Leave>', hide_leave)
        def menu_enter(event):
            self.menu.configure(cursor="hand2", background="green")
        def menu_leave(event):
            self.menu.configure(background="#d8d8d8")
        def menu_click(event):
            self.next.destroy()
            if self.b1 == 0:
                self.background_open()
            if self.m1 == 0:
                self.menu_open()
            if self.l1 == 1:
                self.level_close()
            if self.gb == 1:
                self.game_box_close()
        self.menu = tk.Label(app, borderwidth="0", background="#d8d8d8")
        self.menu.bind('<Enter>', menu_enter)
        self.menu.bind('<Leave>', menu_leave)
        self.menu.bind('<Button-1>', menu_click)
        def retry_enter(event):
            self.retry.configure(cursor="hand2", background="green")
        def retry_leave(event):
            self.retry.configure(background="#d8d8d8")
        def retry_click(event):
            self.re_start()
        self.retry = tk.Label(app, borderwidth="0", background="#d8d8d8")
        self.retry.bind('<Enter>', retry_enter)
        self.retry.bind('<Leave>', retry_leave)
        self.retry.bind('<Button-1>', retry_click)
        def next_enter(event):
            self.next.configure(cursor="hand2", background="green")
        def next_leave(event):
            self.next.configure(background="#d8d8d8")
        self.next = tk.Label(app, borderwidth="0", background="#d8d8d8", image=self._next0)
        self.next.bind('<Enter>', next_enter)
        self.next.bind('<Leave>', next_leave)


        self.game_box_open()

    def game_box_open(self):
        self.gb = 1
        self.box0.place(x=306, y=56, height=160, width=160)
        self.box1.place(x=468, y=56, height=160, width=160)
        self.box2.place(x=630, y=56, height=160, width=160)
        self.box3.place(x=792, y=56, height=160, width=160)
        self.box10.place(x=306, y=218, height=160, width=160)
        self.box11.place(x=468, y=218, height=160, width=160)
        self.box12.place(x=630, y=218, height=160, width=160)
        self.box13.place(x=792, y=218, height=160, width=160)
        self.box20.place(x=306, y=380, height=160, width=160)
        self.box21.place(x=468, y=380, height=160, width=160)
        self.box22.place(x=630, y=380, height=160, width=160)
        self.box23.place(x=792, y=380, height=160, width=160)
        self.box30.place(x=306, y=542, height=160, width=160)
        self.box31.place(x=468, y=542, height=160, width=160)
        self.box32.place(x=630, y=542, height=160, width=160)
        self.box33.place(x=792, y=542, height=160, width=160)
        self.retry.configure(image=self._retry0)
        self.retry.place(x=1094, y=708, height=56, width=56)
        self.menu.configure(image=self._menu0)
        self.menu.place(x=1030, y=708, height=56, width=56)

    def game_box_close(self):
        self.gb = 0
        self.box0.destroy()
        self.opened_box0.destroy()
        self.box1.destroy()
        self.opened_box1.destroy()
        self.box2.destroy()
        self.opened_box2.destroy()
        self.box3.destroy()
        self.opened_box3.destroy()
        self.box10.destroy()
        self.opened_box10.destroy()
        self.box11.destroy()
        self.opened_box11.destroy()
        self.box12.destroy()
        self.opened_box12.destroy()
        self.box13.destroy()
        self.opened_box13.destroy()
        self.box20.destroy()
        self.opened_box20.destroy()
        self.box21.destroy()
        self.opened_box21.destroy()
        self.box22.destroy()
        self.opened_box22.destroy()
        self.box23.destroy()
        self.opened_box23.destroy()
        self.box30.destroy()
        self.opened_box30.destroy()
        self.box31.destroy()
        self.opened_box31.destroy()
        self.box32.destroy()
        self.opened_box32.destroy()
        self.box33.destroy()
        self.opened_box33.destroy()
        self.left0.destroy()
        self.right0.destroy()
        #self.left1.destroy()
        #self.right1.destroy()
        #self.left2.destroy()
        #self.right2.destroy()
        #self.left3.destroy()
        #self.right3.destroy()
        self.menu.destroy()
        self.retry.destroy()
        self.hide.destroy()
        self.next.destroy()

    def create_images(self):
        # SUCCESS
        self._success0 = tk.PhotoImage(file="img/success/success0.png")
        self._success1 = tk.PhotoImage(file="img/success/success1.png")
        self._success2 = tk.PhotoImage(file="img/success/success2.png")
        self._success3 = tk.PhotoImage(file="img/success/success3.png")
        # BUSTED
        self._busted = tk.PhotoImage(file="img/busted/busted_main.png")
        self._busted0_left = tk.PhotoImage(file="img/busted/busted0_left.png")
        self._busted0_right = tk.PhotoImage(file="img/busted/busted0_right.png")
        self._busted1 = tk.PhotoImage(file="img/busted/busted1.png")
        self._busted2 = tk.PhotoImage(file="img/busted/busted2.png")
        self._busted3 = tk.PhotoImage(file="img/busted/busted3.png")
        self._busted4 = tk.PhotoImage(file="img/busted/busted4.png")
        self._busted11 = tk.PhotoImage(file="img/busted/busted11.png")
        self._busted12 = tk.PhotoImage(file="img/busted/busted12.png")
        self._busted13 = tk.PhotoImage(file="img/busted/busted13.png")
        self._busted14 = tk.PhotoImage(file="img/busted/busted14.png")
        self._busted21 = tk.PhotoImage(file="img/busted/busted21.png")
        self._busted22 = tk.PhotoImage(file="img/busted/busted22.png")
        self._busted23 = tk.PhotoImage(file="img/busted/busted23.png")
        self._busted24 = tk.PhotoImage(file="img/busted/busted24.png")
        self._busted31 = tk.PhotoImage(file="img/busted/busted31.png")
        self._busted32 = tk.PhotoImage(file="img/busted/busted32.png")
        self._busted33 = tk.PhotoImage(file="img/busted/busted33.png")
        self._busted34 = tk.PhotoImage(file="img/busted/busted34.png")
        # HACKED LVL
        self._hacked1 = tk.PhotoImage(file="img/level/hacked1.png")
        self._hacked2 = tk.PhotoImage(file="img/level/hacked2.png")
        self._hacked3 = tk.PhotoImage(file="img/level/hacked3.png")
        self._hacked4 = tk.PhotoImage(file="img/level/hacked4.png")
        self._hacked5 = tk.PhotoImage(file="img/level/hacked5.png")
        self._hacked6 = tk.PhotoImage(file="img/level/hacked6.png")
        self._hacked7 = tk.PhotoImage(file="img/level/hacked7.png")
        self._hacked8 = tk.PhotoImage(file="img/level/hacked8.png")
        self._hacked9 = tk.PhotoImage(file="img/level/hacked9.png")
        self._hacked10 = tk.PhotoImage(file="img/level/hacked10.png")
        self._hacked11 = tk.PhotoImage(file="img/level/hacked11.png")
        self._hacked12 = tk.PhotoImage(file="img/level/hacked12.png")
        self._hacked13 = tk.PhotoImage(file="img/level/hacked13.png")
        self._hacked14 = tk.PhotoImage(file="img/level/hacked14.png")
        self._hacked15 = tk.PhotoImage(file="img/level/hacked15.png")
        # SUCCESS LEFT & RIGHT
        #self._success_left = tk.PhotoImage(file="img/success_left.png")
        #self._success_right = tk.PhotoImage(file="img/success_right.png")
        #self._success_left1 = tk.PhotoImage(file="img/success_left1.png")
        #self._success_left2 = tk.PhotoImage(file="img/success_left2.png")
        #self._success_left3 = tk.PhotoImage(file="img/success_left3.png")
        #self._success_left4 = tk.PhotoImage(file="img/success_left4.png")
        #self._success_right1 = tk.PhotoImage(file="img/success_right1.png")
        #self._success_right2 = tk.PhotoImage(file="img/success_right2.png")
        #self._success_right3 = tk.PhotoImage(file="img/success_right3.png")
        #self._success_right4 = tk.PhotoImage(file="img/success_right4.png")
        # MENU - RETRY - NEXT
        self._menu0 = tk.PhotoImage(file="img/moni_menu/menu0.png")
        #self._menu1 = tk.PhotoImage(file="img/menu1.png")
        self._retry0 = tk.PhotoImage(file="img/moni_menu/retry0.png")
        #self._retry1 = tk.PhotoImage(file="img/retry1.png")
        self._next0 = tk.PhotoImage(file="img/moni_menu/next0.png")
        #self._next1 = tk.PhotoImage(file="img/next1.png")
        self._hide0 = tk.PhotoImage(file="img/moni_menu/hide0.png")
        #self._hide1 = tk.PhotoImage(file="img/hide1.png")

    def re_start(self):
        if self.b1 == 1:
            self.background_close()
        if self.gb == 1:
            self.game_box_close()
            self.game_box_create()
            main_support.start_game()
        if self.m1 == 1:
            self.menu_close()
        if self.l1 == 1:
            self.level_close()


if __name__ == '__main__':
    start_gui()
