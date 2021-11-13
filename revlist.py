class ReversedList:
    def __init__(self, lst):
        self.li = list(reversed(lst))

    def __len__(self):
        return len(self.li)

    def __getitem__(self, i):
        return self.li[i]

    def __str__(self):
        return str(self.li)


rl = ReversedList([10])
print(len(rl))
print(rl[0])
