class BellTower:
    def __int__(self, cl1='', cl2=''):
        self.list = []
        self.cl1 = cl1
        self.cl2 = cl2
        self.list.append(self.cl1)
        self.list.append(self.cl2)

    class BigBell:
        def __int__(self):
            self.i = 0

        def __str__(self):
            if self.i == 1:
                self.i = 0
                return 'dong'
            else:
                self.i += 1
                return 'ding'

    class LittleBell:
        def __str__(self):
            return 'ding'

    def append(self, cl):
        self.list.append(cl)

    def sound(self):
        for j in self.list:
            if j == 'BigBell':
                return
            if j == 'LittleBell':
                return
        print('...')


bell_tower = BellTower(BigBell(), LittleBell())
bell_tower.sound()
bell_tower.sound()
bell_tower.append(BigBell())
bell_tower.sound()
bell_tower.sound()
