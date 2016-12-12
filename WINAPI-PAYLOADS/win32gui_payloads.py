import win32api, win32con, win32gui
import random


class WGA:

    def __init__(self):

        self.DESKTOP_DC = win32gui.GetDC(win32gui.GetDesktopWindow())
        self.CURRENT_DC = win32gui.GetDC(win32gui.GetActiveWindow())
        self.NUMBERS_00 = range(1000)
        self.NUMBERS_01 = range(256)

    def chessboard(self):
        while True:
            win32gui.PatBlt(self.CURRENT_DC, random.choice(self.NUMBERS_00), random.choice(self.NUMBERS_00),
                            random.choice(self.NUMBERS_00), random.choice(self.NUMBERS_00), win32con.PATINVERT)

    def display_current_wallpaper(self):
        while True:
            try:
                win32gui.PaintDesktop(self.CURRENT_DC)
            except:
                win32api.Sleep(10**4)

    def display_text(self):
        while True:
            win32api.Sleep(1000)
            words = random.choice(['cunt','lol','fag','dick','_\\|/_','420','ass','pussy','nigger','rekt','bitch','gay',
                                   'owned','faggot','shit','666','MLG','yo','lmao', 'penis','hue', 'XXX','porn','MILF'])
            position = (random.choice(self.NUMBERS_00), random.choice(self.NUMBERS_00),
                        random.choice(self.NUMBERS_00), random.choice(self.NUMBERS_00))
            win32gui.DrawText(self.CURRENT_DC, words, -1, position, win32con.DT_SINGLELINE | win32con.DT_NOCLIP)

    def invert_screen(self):
        while True:
            win32api.Sleep(5000)
            win32gui.PatBlt(self.CURRENT_DC, 0,0,win32api.GetSystemMetrics(0),win32api.GetSystemMetrics(1),
                            win32con.PATINVERT)

    def fairy_dust(self):
        while True:
            win32api.Sleep(1)
            colors = win32api.RGB(random.choice(self.NUMBERS_01), random.choice(self.NUMBERS_01),
                                  random.choice(self.NUMBERS_01))
            win32gui.SetPixel(self.CURRENT_DC, random.choice(range(win32api.GetSystemMetrics(0))),
                              random.choice(range(win32api.GetSystemMetrics(1))), colors)

    def stripes(self):
        while True:
            t = random.choice([0, 1])
            color_1 = random.choice([(0,255,255), (127,255,0), (0,0,0), (255,215,0), (255,0,0),(148,0,211)])
            for y in range(win32api.GetSystemMetrics(1)):
                for x in range(win32api.GetSystemMetrics(0)):
                    if x % 8 == 0:
                        color = win32api.RGB(255,255,255)
                        win32api.Sleep(t)
                    else:
                        color = win32api.RGB(color_1[0],color_1[1],color_1[2])

                    win32gui.SetPixel(self.CURRENT_DC, x, y, color)

    def lines(self):
        while True:
            spacing = random.choice(range(2))
            if spacing == 0:
                for i in range(10**4):
                    win32gui.LineTo(win32gui.GetDC(win32gui.GetActiveWindow()),i,2000)
            else:
                for i in range(10**3):
                    win32gui.LineTo(win32gui.GetDC(win32gui.GetActiveWindow()),i*10,2000)

    def cracked_screen(self):
        while True:
            win32gui.SelectObject(self.CURRENT_DC, win32gui.GetStockObject (win32con.BLACK_BRUSH))
            points = [(random.choice(range(win32api.GetSystemMetrics(0))), random.choice(range(win32api.GetSystemMetrics(1)))),
                      (random.choice(range(win32api.GetSystemMetrics(0))), random.choice(range(win32api.GetSystemMetrics(1)))),
                      (random.choice(range(win32api.GetSystemMetrics(0))), random.choice(range(win32api.GetSystemMetrics(1)))),
                      (random.choice(range(win32api.GetSystemMetrics(0))), random.choice(range(win32api.GetSystemMetrics(1))))]
            win32gui.Polygon(self.CURRENT_DC, points)
            win32api.Beep(10**3,10**2)

    def penis(self):
        while True:
            def balls():
                for y in range (100):
                    for x in range(200):
                        if x % 10 and y % 3:
                            colors = win32api.RGB(153, 76, 0)
                        else:
                            colors = win32api.RGB(255, 178, 102)
                        win32gui.SetPixel(self.CURRENT_DC, int(win32api.GetSystemMetrics(0)/2)+ x,
                                        int(win32api.GetSystemMetrics(1)/2) + y, colors)
            def body():
                for y in range (350):
                    for x in range(100):
                        if y < 50:
                            colors = win32api.RGB(255, 102, 102)

                        else:
                            colors = win32api.RGB(255, 178, 102)

                        win32gui.SetPixel(self.CURRENT_DC, int(win32api.GetSystemMetrics(0)/2 + 50)+ x,
                                        int(win32api.GetSystemMetrics(1)/2 - 350) + y, colors)

            balls()
            body()
