import tkinter, random, ctypes, getpass, winsound, time

class Spooky:
    def __init__(self):
        self.dir = 'C:\\Users\\%s\\Links\\MEDIA\\' % getpass.getuser()

        while True:
            time.sleep(5*60)
            try:
                self.jumpscare()
            except:
                pass


    def jumpscare(self):
        self.root = tkinter.Tk()
        self.root.geometry('%sx%s' % (ctypes.windll.user32.GetSystemMetrics(0),
                                      ctypes.windll.user32.GetSystemMetrics(1)))
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.configure(background = 'black')
        self.a_list = ['s1','s2','s3','s4','s5']
        self.image = tkinter.PhotoImage(file=self.dir+'SCARY\\%s.gif' % random.choice(self.a_list))
        self.label = tkinter.Label(self.root, image = self.image)

        def killer():
            winsound.PlaySound('%sAUDIO\\suicide.wav' % self.dir, winsound.SND_ALIAS)
            self.root.destroy()

        self.label.place(relx=0.5, rely=0.5, anchor='center')
        self.root.after(100,killer)
        self.root.mainloop()


