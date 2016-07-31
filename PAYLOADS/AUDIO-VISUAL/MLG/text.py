import Tkinter, random, thread

class Text:
    def __init__(self):
        thread.start_new_thread(self.movement,())
        while True:
            pass

    def movement(self):

        a_list = list()

        for i in range(500):
            a_list.append(i)


        self.root = Tkinter.Tk()

        self.root.configure(background = 'snow')
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.wm_attributes("-transparentcolor", "snow")

        def update():
            try:
                for j in range(15):
                    self.a_dictionary[j].pack_forget()
                del self.a_dictionary
            except:
                pass

            self.root.geometry('800x800+%s+%s' % (random.choice(a_list), random.choice(a_list)))
            self.a_dictionary = {}

            for i in range(10):

                self.a_dictionary[i] = Tkinter.Label(self.root, text = random.choice(['420','666','LOL','SWEG','PENIS','GAY',
                                                                                      'hue', '_\|/_', 'DOGE', 'c4','CuNt',
                                                                                      'dang', 's2', 'MLG', 'shit', 'ASS']),
                                       font =('Arial', 45), fg = random.choice(['red', 'green', 'white',
                                                                                'black','yellow','blue']),
                                       background = 'snow')

                self.a_dictionary[i].pack(side = random.choice(['right', 'left', 'bottom', 'top']),
                                          anchor = random.choice(['nw','n', 'ne', 'w', 'center',
                                                                  'e', 'sw', 's', 'se']))

            self.root.after(200, update)

        update()
        self.root.mainloop()


zz = Text()

