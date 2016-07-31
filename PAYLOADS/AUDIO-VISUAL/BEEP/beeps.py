import winsound, random

class Beeps:
    def __init__(self):
        self.sound()

    def sound(self):
        self.list = list()

        for i in range(37,2500):
            self.list.append(i)

        while True:
            winsound.Beep(random.choice(self.list), 100)


zz = Beeps()
