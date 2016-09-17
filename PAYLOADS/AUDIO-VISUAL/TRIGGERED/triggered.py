import Tkinter, ctypes, pyHook, pythoncom, thread, getpass, os, winsound, ImageTk, random

class SWJ():
    def __init__(self):
        self.resolution = [ctypes.windll.user32.GetSystemMetrics(0),
                           ctypes.windll.user32.GetSystemMetrics(1)]
        self.lst = list()
        self.dir = 'C:\Users\%s\Links\MEDIA\\' % getpass.getuser()
        self.a = False

        def counter():
            self.m = 0
            for i in range(3):
                self.lst.append('%s.gif' % i)

        counter()


        thread.start_new_thread(self.mouse_hook,())
        while True:
            pass


    def bar(self):
        self.root = Tkinter.Tk()
        self.root.configure(background='snow')
        self.root.overrideredirect(True)
        self.root.wm_attributes("-transparentcolor", "snow")

        bar_widget = Tkinter.Toplevel(self.root)
        bar_widget.title(self.m)
        bar_widget.configure(background='snow')
        bar_widget.wm_attributes("-transparentcolor", "snow")
        bar_widget.geometry('420x85+%s+%s'%(0, 0))
        bar_widget.overrideredirect(True)
        bar_widget.attributes("-topmost", True)

        img = Tkinter.PhotoImage(file = '%sSWJ\\BAR\\%s' %(self.dir,self.lst[self.m - 1]))
        img_l = Tkinter.Label(bar_widget, image= img, background = 'snow')
        img_l.pack()

        self.root.after(100,self.mouse_hook)
        self.root.mainloop()

    def triggered(self):
        self.soundbgcode = '''Set Sound = CreateObject("WMPlayer.OCX.7")
                Sound.URL = "%sAUDIO\\gender.wav"
                Sound.Controls.play
                do while Sound.currentmedia.duration = 0
                wscript.sleep 100
                loop
                wscript.sleep (int(Sound.currentmedia.duration)+1)*1000
                ''' % (self.dir)

        self.sbgcodew = open(self.dir + "OTHER\\sound.vbs", 'w')
        self.sbgcodew.write(self.soundbgcode)
        self.sbgcodew.close()
        os.system('start %sOTHER\\sound.vbs' % self.dir)

        if self.a == False:
            self.a = True
            self.movement('C:\Users\%s\Links\MEDIA\SWJ\TRIGGER\\' % getpass.getuser(),4)



    def mouse_hook(self):

        def on_click(event):

            if event.Message == 514:

                try:
                    self.root.destroy()
                except:
                    pass

                self.m += 1

                if self.m == 1:
                    winsound.Beep(1000,600)
                    self.bar()
                elif self.m == 2:
                    winsound.Beep(1900,600)
                    self.bar()
                elif self.m == 3:
                    winsound.Beep(2800,600)
                    self.bar()
                else:
                    self.triggered()

                return True


        hm = pyHook.HookManager()
        hm.MouseAll = on_click
        hm.HookMouse()
        pythoncom.PumpMessages()

    def movement(self, path, frame_number, side=0):
        while True:
            try:
                for self.vv in range(int(frame_number)):
                    self.root = Tkinter.Tk()

                    if side == 0:

                        self.root.geometry('950x500+350+350')

                    else:

                        a = ctypes.windll.user32.GetSystemMetrics(0)/2
                        c = '950x500+%s+%s' % (str(a), 0)
                        self.root.geometry(c)

                    self.root.configure(bg='snow')

                    self.root.overrideredirect(True)
                    self.root.wm_attributes("-transparentcolor", "snow")

                    self.can = Tkinter.Canvas(width=950, height=500, bg='snow', bd=False,
                                          highlightthickness=0)
                    self.img = ImageTk.PhotoImage(file=path + '%s.gif' % (self.vv))
                    self.can.create_image(425, 300, image=self.img)

                    self.can.pack(expand=True, fill='both')

                    def restart():
                        if self.vv == frame_number:
                            self.vv = 0
                            self.can.pack_forget()
                            self.root.destroy()
                        else:
                            self.can.pack_forget()
                            self.root.quit()



                    self.root.attributes("-topmost", True)
                    self.root.after(25, restart)
                    self.root.mainloop()
            except:
                rand_t = random.choice([5,7,2])
                if rand_t % 2 ==0:
                    os.system('start %sOTHER\\sound.vbs' % self.dir)
                else:
                    pass


zz = SWJ()
