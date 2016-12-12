import tkinter, ctypes, random, hashlib, getpass, winsound

class Nerdy:
    def __init__(self):
        self.halt = 0

        while self.halt !=1:
            self.question_widget()

    def question_widget(self):

        def verify(event):
            d = self.box.get()

            if d == self.a:
                self.halt = 1
                self.root.quit()
                quit()
            elif d == 'danooct1':
                self.halt = 1
                self.root.quit()
                quit()
            else:
                winsound.Beep(800, 250)


        self.root = tkinter.Tk()
        self.root.configure(background= 'black')

        self.root.geometry('%sx%s' % (ctypes.windll.user32.GetSystemMetrics(0),
                                 ctypes.windll.user32.GetSystemMetrics(1)))

        self.root.attributes("-topmost", True)
        self.root.overrideredirect(True)

        self.label = tkinter.Label(self.root, background='black', fg='white',
                                   text='In order to continue, please decrypt the following hash:')
        self.label.pack()

        self.label_2 = tkinter.Label(self.root, background='black', fg='white', text=self.question())
        self.label_2.pack()

        self.box = tkinter.Entry(width= 70)
        self.box.pack()

        self.box.bind("<Return>", verify)

        self.root.mainloop()

    def question(self):

        def number():
            a_list = list()
            b_list = ['OL22b23', '0n1gG4', 'j44I3tty', 'FHEY8hggu', 'S0mb74HP', '3455ttRRf', 'oop0L33r', '00IIt9y',
                      'qdg554mb', '22334gghj', 'fh34457r2', 'ggh77jjp', 'rrt566789JJ', '8Z97jG', 'AAA009ii8gt', '1nurL']
            for i in range(1000):
                a_list.append(i)


            a_number = abs(random.choice(a_list) * (random.choice(a_list) - random.choice(a_list)) + random.choice(a_list))
            a_pass = random.choice(b_list) + str(random.choice(a_list)) + \
                     str(getpass.getuser()) + str(a_number) + random.choice(b_list) + str(random.choice(a_list))

            return a_pass


        def a_hash(number):

            if random.choice([1,2,3,5,7]) % 2 == 0:
                return hashlib.md5(number)
            elif random.choice([1,2,3,5,7]) % 3 == 0:
                return hashlib.sha384(number)
            elif random.choice([1, 2, 3, 5, 7]) % 5 == 0:
                return hashlib.sha256(number)
            elif random.choice([1, 2, 3, 5, 7]) % 7 == 0:
                return hashlib.sha1(number)
            else:
                return hashlib.sha512(number)


        self.a = number()
        self.h = str(a_hash(self.a.encode('utf-8')).hexdigest())

        return self.h

